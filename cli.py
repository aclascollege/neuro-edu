"""
ACLAS Neuro-Edu CLI
Usage:
    python cli.py simulate --text "Quantum mechanics" --complexity 0.8
    python cli.py train --epochs 10
    python cli.py report
    python cli.py reset
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import argparse
from neuro_edu.engine import UltimateClassroom


def print_header():
    print("\n" + "="*60)
    print("  ACLAS NEURO-EDU  |  Cognitive Simulation Engine v3.0")
    print("="*60 + "\n")


def cmd_simulate(args):
    """Run a simulation broadcast."""
    print_header()
    classroom = UltimateClassroom()
    classroom.setup(args.agents)
    print(f"  Classroom initialized: {args.agents} agents")
    print(f"  Instruction: '{args.text[:50]}...' " if len(args.text) > 50 else f"  Instruction: '{args.text}'")
    print(f"  Complexity:  {args.complexity}")
    print(f"  Domain:      {args.domain}\n")

    skills = {args.domain: 0.8}
    result = classroom.broadcast(args.text, args.complexity, skills)

    print(f"  Tick #{result['tick']} complete — {result['cascade_events']} cascade events fired\n")
    print(f"  {'Agent':<20} {'Mood':<12} {'Absorption':>10}  Thought")
    print("  " + "-"*80)
    for a in result["agents"]:
        thought_short = a["thought"][:45] + "..." if len(a["thought"]) > 45 else a["thought"]
        print(f"  {a['name']:<20} {a['mood']:<12} {a['prob']:>10.3f}  {thought_short}")

    # Metrics
    metrics = classroom.get_metrics()
    print(f"\n  GPA: {metrics['gpa']:.2f}/4.0   CAS: {metrics['cas']:.4f}   "
          f"Retention: {metrics['retention_rate']:.1%}   Diversity: {metrics['diversity_index']:.3f}")

    at_risk = metrics.get("dropout_risk", [])
    if at_risk:
        print(f"\n  ⚠ At-Risk Agents ({len(at_risk)}):")
        for r in at_risk[:3]:
            print(f"    · {r['name']} — Risk: {r['risk']:.3f} [{r['mood']}]")
    print()


def cmd_train(args):
    """Run federated training."""
    print_header()
    classroom = UltimateClassroom()
    classroom.setup(20)

    if not classroom._dataset:
        print("  ERROR: No training data found in data/knowledge_base.json")
        return

    print(f"  Dataset: {len(classroom._dataset)} samples")
    print(f"  Agents:  {len(classroom.agents)}")
    print(f"  Epochs:  {args.epochs}\n")

    result = classroom.run_training(epochs=args.epochs)

    print("  Epoch  Loss")
    print("  " + "-"*20)
    for i, loss in enumerate(result["epoch_losses"], 1):
        bar = "█" * int((1 - loss) * 30)
        print(f"  {i:>5}  {loss:.6f}  {bar}")

    print(f"\n  Final loss: {result['final_loss']:.6f}")
    print("  Training complete.\n")


def cmd_report(args):
    """Print a full classroom metrics report."""
    print_header()
    classroom = UltimateClassroom()
    classroom.setup(20)
    # Run a few ticks first
    for _ in range(3):
        classroom.broadcast("Sample lesson content for evaluation.", 0.5, {"logic": 0.5})

    metrics = classroom.get_metrics()
    print("  ┌─ ACLAS Cognitive Evaluation Report ─────────────────────┐")
    print(f"  │  Tick:             {metrics['tick']}")
    print(f"  │  GPA:              {metrics['gpa']:.2f} / 4.00")
    print(f"  │  CAS Score:        {metrics['cas']:.4f}")
    print(f"  │  Retention Rate:   {metrics['retention_rate']:.1%}")
    print(f"  │  Diversity Index:  {metrics['diversity_index']:.4f} (Shannon H)")
    print("  ├─ Mood Distribution ─────────────────────────────────────┤")
    for mood, count in metrics["mood_distribution"].items():
        bar = "▓" * count
        print(f"  │  {mood:<10} {bar:<25} ({count})")
    print("  ├─ Skill Distribution ────────────────────────────────────┤")
    for skill, val in metrics["skill_distribution"].items():
        bar = "█" * int(val * 20)
        print(f"  │  {skill:<10} {bar:<22} {val:.3f}")
    at_risk = metrics.get("dropout_risk", [])
    if at_risk:
        print("  ├─ Dropout Risk ───────────────────────────────────────────┤")
        for r in at_risk:
            print(f"  │  ⚠ {r['name']:<15} Risk: {r['risk']:.3f} [{r['mood']}]")
    print("  └─────────────────────────────────────────────────────────┘\n")


def main():
    parser = argparse.ArgumentParser(
        prog="acs",
        description="ACLAS Cognitive Simulation CLI"
    )
    subparsers = parser.add_subparsers(dest="command")

    # simulate
    sim = subparsers.add_parser("simulate", help="Run a simulation broadcast")
    sim.add_argument("--text", default="Introduction to machine learning fundamentals.")
    sim.add_argument("--complexity", type=float, default=0.5)
    sim.add_argument("--domain", default="logic", choices=["logic", "math", "language", "memory", "creative"])
    sim.add_argument("--agents", type=int, default=20)

    # train
    tr = subparsers.add_parser("train", help="Run federated training on dataset")
    tr.add_argument("--epochs", type=int, default=5)

    # report
    subparsers.add_parser("report", help="Print full evaluation report")

    args = parser.parse_args()

    if args.command == "simulate":
        cmd_simulate(args)
    elif args.command == "train":
        cmd_train(args)
    elif args.command == "report":
        cmd_report(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
