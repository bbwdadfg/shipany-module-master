#!/usr/bin/env python3
"""Analyze ShipAny module dependencies"""
import argparse

# Module dependency map
DEPENDENCIES = {
    "landing-page": {
        "required": [],
        "optional": ["internationalization", "themes"]
    },
    "user-center": {
        "required": ["database", "auth"],
        "optional": ["rbac", "internationalization", "themes"]
    },
    "admin-dashboard": {
        "required": ["database", "auth", "rbac"],
        "optional": ["internationalization", "themes"]
    },
    "database": {
        "required": [],
        "optional": []
    },
    "auth": {
        "required": ["database"],
        "optional": []
    },
    "rbac": {
        "required": ["database", "auth"],
        "optional": []
    },
    "internationalization": {
        "required": [],
        "optional": []
    },
    "themes": {
        "required": [],
        "optional": []
    },
    "documentation": {
        "required": [],
        "optional": ["internationalization"]
    },
    "credits": {
        "required": ["database", "auth"],
        "optional": []
    },
    "payment": {
        "required": ["database", "auth"],
        "optional": ["credits"]
    },
    "storage": {
        "required": [],
        "optional": ["auth"]
    },
    "email": {
        "required": [],
        "optional": []
    },
    "ai": {
        "required": [],
        "optional": ["credits", "auth"]
    },
    "analytics": {
        "required": [],
        "optional": []
    },
    "advertising": {
        "required": [],
        "optional": []
    },
    "affiliate": {
        "required": ["database", "auth"],
        "optional": []
    },
    "customer-service": {
        "required": [],
        "optional": []
    }
}

def get_all_dependencies(modules, include_optional=False):
    """Recursively get all dependencies for given modules"""
    all_deps = set()
    to_process = set(modules)

    while to_process:
        module = to_process.pop()
        if module in all_deps or module not in DEPENDENCIES:
            continue

        all_deps.add(module)
        deps = DEPENDENCIES[module]["required"]
        if include_optional:
            deps += DEPENDENCIES[module]["optional"]

        for dep in deps:
            if dep not in all_deps:
                to_process.add(dep)

    return all_deps

def main():
    parser = argparse.ArgumentParser(description="Analyze ShipAny module dependencies")
    parser.add_argument("--modules", nargs="+", required=True, help="Modules to analyze")
    parser.add_argument("--include-optional", action="store_true", help="Include optional dependencies")
    args = parser.parse_args()

    # Validate modules
    invalid = [m for m in args.modules if m not in DEPENDENCIES]
    if invalid:
        print(f"❌ Invalid modules: {', '.join(invalid)}")
        print(f"\nAvailable modules:")
        for module in sorted(DEPENDENCIES.keys()):
            print(f"  - {module}")
        return 1

    # Get all dependencies
    all_modules = get_all_dependencies(args.modules, args.include_optional)
    requested = set(args.modules)
    required_deps = all_modules - requested

    print(f"\n📦 Dependency Analysis for: {', '.join(args.modules)}\n")
    print(f"{'='*60}\n")

    print(f"✅ Requested Modules ({len(requested)}):")
    for module in sorted(requested):
        print(f"   • {module}")

    if required_deps:
        print(f"\n⚠️  Required Dependencies ({len(required_deps)}):")
        for module in sorted(required_deps):
            print(f"   • {module}")

    print(f"\n📋 Complete Module List ({len(all_modules)}):")
    for module in sorted(all_modules):
        marker = "✓" if module in requested else "→"
        print(f"   {marker} {module}")

    print(f"\n{'='*60}\n")
    print(f"Total modules to extract: {len(all_modules)}")

    return 0

if __name__ == "__main__":
    exit(main())
