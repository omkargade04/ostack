"""Give every ostack skill a bare `/name` next to `/ostack:name`.

Claude Code drops a plugin skill whose SKILL.md realpath equals a user-level
skill's realpath, so a symlink into this repo hides `/ostack:name`. Each bare
skill is therefore a small real file that copies the menu fields and points
at the repo skill. Re-run after adding a skill or changing a description.
Bare wrappers set disable-model-invocation, so the model sees each skill once.
"""

import pathlib
import sys

REPO_SKILLS = pathlib.Path(__file__).resolve().parent.parent / "skills"
USER_SKILLS = pathlib.Path.home() / ".claude" / "skills"
KEEP_ORIGINAL = {"grill-me"}
MENU_KEYS = ("name", "description")


def frontmatter_lines(skill_md):
    lines = skill_md.read_text().splitlines()
    if not lines or lines[0] != "---":
        sys.exit(f"{skill_md}: no frontmatter")
    end = lines.index("---", 1)
    return lines[1:end]


def menu_fields(lines):
    kept = []
    keeping = False
    for line in lines:
        if line and not line[0].isspace():
            keeping = line.split(":", 1)[0] in MENU_KEYS
        if keeping:
            kept.append(line)
    return kept


def pointer(skill_dir):
    return f"Read `{skill_dir / 'SKILL.md'}` and follow it."


def wrapper(skill_dir):
    fields = menu_fields(frontmatter_lines(skill_dir / "SKILL.md"))
    return "\n".join(
        [
            "---",
            *fields,
            "disable-model-invocation: true",
            "---",
            "",
            f"{pointer(skill_dir)} Resolve its relative paths from `{skill_dir}`.",
            "",
        ]
    )


def is_ours(target, skill_dir):
    if target.is_symlink():
        return target.resolve() == skill_dir.resolve()
    skill_md = target / "SKILL.md"
    return skill_md.is_file() and pointer(skill_dir) in skill_md.read_text()


def main():
    for skill_dir in sorted(
        p for p in REPO_SKILLS.iterdir() if (p / "SKILL.md").is_file()
    ):
        name = skill_dir.name
        if name in KEEP_ORIGINAL:
            continue
        target = USER_SKILLS / name
        if target.exists() or target.is_symlink():
            if not is_ours(target, skill_dir):
                print(f"skip {name}: {target} is not an ostack wrapper")
                continue
            if target.is_symlink():
                target.unlink()
        target.mkdir(exist_ok=True)
        (target / "SKILL.md").write_text(wrapper(skill_dir))
        print(f"wrote {name}")


if __name__ == "__main__":
    main()
