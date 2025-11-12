# OpenCORE-Skills
**COllaborative REpository for Physical AI and Robotics Skills**

This is an open repository and catalog for defining a common language for *Skills* in robotics and Physical AI.

The goal of OpenCORE is to create a set of standardized, machine- and human-readable definitions that allow different systems (robots, AI software, orchestration systems) to communicate about capabilities in an interoperable way.

## 🚀 View the Live Catalog

The skill catalog is searchable and browsable on our GitHub Page:
**[https://YOUR-USERNAME.github.io/opencore-skills/](https://YOUR-USERNAME.github.io/opencore-skills/)**

## 🧬 Anatomy of a Skill

An OpenCORE *Skill* is defined as a simple YAML file with four main fields:

* `name`: The unique, single-word identifier (e.g., `pick`).
* `domain_tags`: Broad categories of the action (e.g., `manipulation`, `navigation`).
* `mission_tags`: The goal or use case for the skill (e.g., `pick_and_place`, `logistics`).
* `description`: A clear text description of what the skill does.

### Example (`pick.yaml`)

```yaml
name: pick
domain_tags: [manipulation, grasping]
mission_tags: [pick_and_place, bin_picking, logistics]
description: Senses and grasps a target object from a specified location.
