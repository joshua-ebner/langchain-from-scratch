"""
Simple business analytics utilities.

This module contains helper functions and classes that might exist
in an internal analytics or data platform codebase.
"""

from typing import List


class FinancialMetrics:
    """
    Utility class for calculating common business metrics.
    """

    def __init__(self, revenue: float, variable_costs: float):
        self.revenue = revenue
        self.variable_costs = variable_costs

    def contribution_margin(self) -> float:
        """
        Calculate contribution margin.

        Contribution margin = revenue - variable costs
        """
        return self.revenue - self.variable_costs

    def contribution_margin_ratio(self) -> float:
        """
        Calculate contribution margin ratio.
        """
        if self.revenue == 0:
            return 0.0
        return self.contribution_margin() / self.revenue


def summarize_metrics(metrics: List[FinancialMetrics]) -> dict:
    """
    Aggregate contribution margin metrics across products.
    """
    total_revenue = sum(m.revenue for m in metrics)
    total_margin = sum(m.contribution_margin() for m in metrics)

    return {
        "total_revenue": total_revenue,
        "total_contribution_margin": total_margin,
    }


def main():
    products = [
        FinancialMetrics(revenue=100_000, variable_costs=40_000),
        FinancialMetrics(revenue=75_000, variable_costs=30_000),
    ]

    summary = summarize_metrics(products)
    print("Portfolio summary:")
    print(summary)


if __name__ == "__main__":
    main()
