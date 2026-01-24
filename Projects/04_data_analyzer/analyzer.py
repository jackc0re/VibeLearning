"""
Data Analyzer
=============
Load, analyze, filter, sort, and visualize data from CSV and JSON files.
"""

import csv
import json
import math
from statistics import mean, median
from collections import Counter
from typing import List, Dict, Union, Optional


class DataAnalyzer:
    """Main data analyzer class."""
    
    def __init__(self):
        self.data = []
        self.headers = []
        self.filename = None
    
    def load_csv(self, filename):
        """Load data from CSV file."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.headers = reader.fieldnames or []
                self.data = [row for row in reader]
                self.filename = filename
            print(f"Loaded {len(self.data)} records from {filename}")
            return True
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return False
    
    def load_json(self, filename):
        """Load data from JSON file."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    self.data = data
                    if data:
                        self.headers = list(data[0].keys())
                else:
                    self.data = [data]
                    self.headers = list(data.keys())
                self.filename = filename
            print(f"Loaded {len(self.data)} records from {filename}")
            return True
        except Exception as e:
            print(f"Error loading JSON: {e}")
            return False
    
    def load_from_dict_list(self, data: List[Dict]):
        """Load data from a list of dictionaries."""
        if not data:
            print("Error: Empty data provided")
            return False
        
        self.data = data
        self.headers = list(data[0].keys())
        print(f"Loaded {len(self.data)} records from memory")
        return True
    
    def display_data(self, limit=10):
        """Display data rows."""
        if not self.data:
            print("No data to display.")
            return
        
        display_count = min(limit, len(self.data)) if limit else len(self.data)
        
        print(f"\nDisplaying {display_count} of {len(self.data)} records:")
        print("=" * 80)
        
        col_widths = {}
        for header in self.headers:
            col_widths[header] = max(len(header), 15)
        
        header_row = " | ".join(f"{header:<{col_widths[header]}}" for header in self.headers)
        print(header_row)
        print("-" * 80)
        
        for i, row in enumerate(self.data[:display_count]):
            values = []
            for header in self.headers:
                value = str(row.get(header, ''))[:col_widths[header] - 1]
                values.append(f"{value:<{col_widths[header]}}")
            print(" | ".join(values))
        
        if display_count < len(self.data):
            print(f"\n... and {len(self.data) - display_count} more records.")
        
        print("=" * 80)
    
    def get_columns(self):
        """Get list of column names."""
        return list(self.headers)
    
    def is_numeric_column(self, column):
        """Check if a column contains numeric data."""
        if not self.data or column not in self.headers:
            return False
        
        for row in self.data:
            value = row.get(column)
            if value is not None and value != '':
                try:
                    float(value)
                except (ValueError, TypeError):
                    return False
        
        return True
    
    def get_numeric_values(self, column):
        """Extract numeric values from a column."""
        values = []
        for row in self.data:
            value = row.get(column)
            if value is not None and value != '':
                try:
                    values.append(float(value))
                except (ValueError, TypeError):
                    pass
        return values
    
    def get_unique_values(self, column):
        """Get unique values from a column."""
        values = set()
        for row in self.data:
            value = row.get(column)
            if value is not None:
                values.add(value)
        return sorted(list(values))
    
    def calculate_statistics(self, column):
        """Calculate comprehensive statistics for a numeric column."""
        if not self.is_numeric_column(column):
            return None
        
        values = self.get_numeric_values(column)
        
        if not values:
            return None
        
        values_sorted = sorted(values)
        n = len(values)
        
        stats = {
            'count': n,
            'mean': sum(values) / n,
            'median': median(values),
            'mode': self.get_mode(column),
            'min': min(values),
            'max': max(values),
            'range': max(values) - min(values),
            'sum': sum(values),
            'std_dev': self.calculate_std_dev(values),
            'variance': self.calculate_variance(values),
            'q1': self.calculate_percentile(values_sorted, 25),
            'q2': median(values),
            'q3': self.calculate_percentile(values_sorted, 75),
            'iqr': None
        }
        
        stats['iqr'] = stats['q3'] - stats['q1']
        
        return stats
    
    def get_mode(self, column):
        """Get the mode(s) of a column."""
        values = [row.get(column) for row in self.data if row.get(column) is not None]
        
        if not values:
            return None
        
        counter = Counter(values)
        max_count = max(counter.values())
        modes = [value for value, count in counter.items() if count == max_count]
        
        return modes[0] if len(modes) == 1 else modes
    
    def calculate_std_dev(self, values):
        """Calculate standard deviation."""
        if len(values) < 2:
            return 0
        avg = sum(values) / len(values)
        variance = sum((val - avg) ** 2 for val in values) / (len(values) - 1)
        return math.sqrt(variance)
    
    def calculate_variance(self, values):
        """Calculate variance."""
        if len(values) < 2:
            return 0
        avg = sum(values) / len(values)
        return sum((val - avg) ** 2 for val in values) / (len(values) - 1)
    
    def calculate_percentile(self, values_sorted, percentile):
        """Calculate percentile."""
        if not values_sorted:
            return None
        
        n = len(values_sorted)
        k = (n - 1) * percentile / 100
        f = math.floor(k)
        c = math.ceil(k)
        
        if f == c:
            return values_sorted[int(k)]
        
        d0 = values_sorted[int(f)] * (c - k)
        d1 = values_sorted[int(c)] * (k - f)
        
        return d0 + d1
    
    def filter_equals(self, column, value):
        """Filter rows where column equals value."""
        filtered = [row for row in self.data if row.get(column) == value]
        return filtered
    
    def filter_greater_than(self, column, value):
        """Filter rows where numeric column > value."""
        filtered = []
        for row in self.data:
            try:
                if float(row.get(column, 0)) > value:
                    filtered.append(row)
            except (ValueError, TypeError):
                pass
        return filtered
    
    def filter_less_than(self, column, value):
        """Filter rows where numeric column < value."""
        filtered = []
        for row in self.data:
            try:
                if float(row.get(column, 0)) < value:
                    filtered.append(row)
            except (ValueError, TypeError):
                pass
        return filtered
    
    def filter_contains(self, column, substring: str, case_sensitive=False):
        """Filter rows where column contains substring."""
        substring = str(substring)
        
        filtered = []
        for row in self.data:
            value = str(row.get(column, ''))
            
            if not case_sensitive:
                if substring.lower() in value.lower():
                    filtered.append(row)
            else:
                if substring in value:
                    filtered.append(row)
        
        return filtered
    
    def filter_between(self, column, min_val, max_val):
        """Filter rows where numeric column is between min and max."""
        filtered = []
        for row in self.data:
            try:
                value = float(row.get(column, 0))
                if min_val <= value <= max_val:
                    filtered.append(row)
            except (ValueError, TypeError):
                pass
        return filtered
    
    def sort_by_column(self, column, reverse=False):
        """Sort data by column."""
        try:
            if self.is_numeric_column(column):
                self.data.sort(key=lambda x: float(x.get(column, 0)), reverse=reverse)
            else:
                self.data.sort(key=lambda x: str(x.get(column, '')), reverse=reverse)
            return True
        except Exception as e:
            print(f"Error sorting: {e}")
            return False
    
    def display_histogram(self, column, bins=10):
        """Display histogram of numeric column."""
        if not self.is_numeric_column(column):
            print(f"Column '{column}' is not numeric")
            return
        
        values = self.get_numeric_values(column)
        
        if not values:
            print(f"No numeric values in column '{column}'")
            return
        
        min_val, max_val = min(values), max(values)
        bin_width = (max_val - min_val) / bins if min_val != max_val else 1
        
        print(f"\nHistogram of '{column}' ({len(values)} values)")
        print("=" * 60)
        
        bins_data = []
        for i in range(bins):
            bin_start = min_val + (i * bin_width)
            bin_end = min_val + ((i + 1) * bin_width)
            
            if i == bins - 1:
                bin_end = max_val + 0.001
            
            count = sum(1 for v in values if bin_start <= v < bin_end)
            bins_data.append({
                'range': (bin_start, bin_end),
                'count': count,
                'percentage': (count / len(values)) * 100
            })
        
        max_count = max(item['count'] for item in bins_data) if bins_data else 1
        
        for i, bin_data in enumerate(bins_data):
            range_str = f"[{bin_data['range'][0]:.2f}, {bin_data['range'][1]:.2f})"
            bar_length = int((bin_data['count'] / max_count) * 40)
            bar = '█' * bar_length
            print(f"{range_str:20s} | {bin_data['count']:5d} {bar} {bin_data['percentage']:5.1f}%")
        
        print("=" * 60)
    
    def display_bar_chart(self, column, top_n=20):
        """Display bar chart for categorical data."""
        if not self.data or column not in self.headers:
            print(f"No data for column '{column}'")
            return
        
        values = [row.get(column) for row in self.data if row.get(column) is not None]
        
        if not values:
            print(f"No values in column '{column}'")
            return
        
        counter = Counter(values)
        top_items = counter.most_common(top_n)
        
        print(f"\nBar Chart of '{column}' (Top {len(top_items)})")
        print("=" * 60)
        
        max_count = max(count for _, count in top_items) if top_items else 1
        
        for label, count in top_items:
            label_str = str(label)[:30]
            bar_length = int((count / max_count) * 40)
            bar = '█' * bar_length
            print(f"{label_str:30s} | {count:5d} {bar}")
        
        print("=" * 60)
    
    def generate_summary_report(self):
        """Generate a comprehensive summary report."""
        report = []
        report.append("=" * 80)
        report.append(" " * 25 + "DATA ANALYSIS REPORT")
        report.append("=" * 80)
        report.append(f"\nSource File: {self.filename or 'In-memory data'}")
        report.append(f"Total Records: {len(self.data)}")
        report.append(f"Columns: {', '.join(self.headers)}")
        
        report.append("\n" + "-" * 80)
        report.append("COLUMN STATISTICS")
        report.append("-" * 80)
        
        for column in self.headers:
            if self.is_numeric_column(column):
                stats = self.calculate_statistics(column)
                if stats:
                    report.append(f"\n{column}:")
                    report.append(f"  Count:   {stats['count']}")
                    report.append(f"  Mean:    {stats['mean']:.2f}")
                    report.append(f"  Median:  {stats['median']:.2f}")
                    report.append(f"  Mode:    {stats['mode']}")
                    report.append(f"  Min:     {stats['min']:.2f}")
                    report.append(f"  Max:     {stats['max']:.2f}")
                    report.append(f"  StdDev:  {stats['std_dev']:.2f}")
                    report.append(f"  Range:   [{stats['q1']:.2f}, {stats['q3']:.2f}]")
            else:
                values = [row.get(column) for row in self.data if row.get(column) is not None]
                unique_count = len(set(values))
                report.append(f"\n{column}:")
                report.append(f"  Count:      {len(values)}")
                report.append(f"  Unique:     {unique_count}")
                report.append(f"  Most Common: {self.get_mode(column)}")
        
        report.append("\n" + "=" * 80)
        
        return '\n'.join(report)
    
    def save_report(self, filename):
        """Save report to file."""
        report = self.generate_summary_report()
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"Report saved to {filename}")
            return True
        except Exception as e:
            print(f"Error saving report: {e}")
            return False
    
    def export_to_json(self, filename):
        """Export data to JSON file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2)
            print(f"Data exported to {filename}")
            return True
        except Exception as e:
            print(f"Error exporting to JSON: {e}")
            return False
    
    def export_to_csv(self, filename):
        """Export data to CSV file."""
        try:
            with open(filename, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.headers)
                writer.writeheader()
                writer.writerows(self.data)
            print(f"Data exported to {filename}")
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False


def display_menu():
    """Display main menu."""
    print("\n" + "=" * 40)
    print("     DATA ANALYZER MENU")
    print("=" * 40)
    print("1. Load Data (CSV)")
    print("2. Load Data (JSON)")
    print("3. View Data")
    print("4. View Column Statistics")
    print("5. Filter Data")
    print("6. Sort Data")
    print("7. Generate Histogram")
    print("8. Generate Bar Chart")
    print("9. Generate Report")
    print("10. Export Data (CSV)")
    print("11. Export Data (JSON)")
    print("12. Exit")
    print("=" * 40)


def get_column_choice(prompt, analyzer):
    """Get column choice from user."""
    if not analyzer.headers:
        print("No data loaded. Please load data first.")
        return None
    
    print("\nAvailable columns:")
    for i, column in enumerate(analyzer.headers, 1):
        is_numeric = " (numeric)" if analyzer.is_numeric_column(column) else ""
        print(f"{i}. {column}{is_numeric}")
    
    try:
        choice = int(input(f"\n{prompt} (1-{len(analyzer.headers)}): "))
        if 1 <= choice <= len(analyzer.headers):
            return analyzer.headers[choice - 1]
        print("Invalid choice.")
        return None
    except ValueError:
        print("Please enter a number.")
        return None


def main():
    """Main application function."""
    analyzer = DataAnalyzer()
    
    print("=" * 40)
    print("      DATA ANALYZER")
    print("=" * 40)
    print("Load, analyze, and visualize your data!")
    print("=" * 40)
    
    while True:
        display_menu()
        
        if analyzer.data:
            print(f"\nData: {len(analyzer.data)} records from {analyzer.filename or 'memory'}")
        
        try:
            choice = input("\nEnter your choice (1-12): ").strip()
            
            if not choice.isdigit():
                print("Please enter a number.")
                continue
            
            choice = int(choice)
            
            if choice == 1:
                filename = input("Enter CSV filename: ").strip()
                if analyzer.load_csv(filename):
                    print(f"Successfully loaded CSV!")
            
            elif choice == 2:
                filename = input("Enter JSON filename: ").strip()
                if analyzer.load_json(filename):
                    print(f"Successfully loaded JSON!")
            
            elif choice == 3:
                if not analyzer.data:
                    print("No data loaded. Please load data first.")
                else:
                    try:
                        limit = int(input("Enter number of rows to display (0 for all): ") or "10")
                        analyzer.display_data(limit)
                    except ValueError:
                        analyzer.display_data(10)
            
            elif choice == 4:
                column = get_column_choice("Select column", analyzer)
                if column:
                    if analyzer.is_numeric_column(column):
                        stats = analyzer.calculate_statistics(column)
                        if stats:
                            print(f"\nStatistics for '{column}':")
                            print("=" * 50)
                            print(f"  Count:    {stats['count']}")
                            print(f"  Mean:     {stats['mean']:.2f}")
                            print(f"  Median:   {stats['median']:.2f}")
                            print(f"  Mode:     {stats['mode']}")
                            print(f"  Min:      {stats['min']:.2f}")
                            print(f"  Max:      {stats['max']:.2f}")
                            print(f"  Range:    {stats['range']:.2f}")
                            print(f"  Std Dev:  {stats['std_dev']:.2f}")
                            print(f"  Variance: {stats['variance']:.2f}")
                            print(f"  Q1 (25%): {stats['q1']:.2f}")
                            print(f"  Q2 (50%): {stats['q2']:.2f}")
                            print(f"  Q3 (75%): {stats['q3']:.2f}")
                            print(f"  IQR:      {stats['iqr']:.2f}")
                            print("=" * 50)
                    else:
                        print(f"\nStatistics for '{column}' (Categorical):")
                        print("=" * 50)
                        print(f"  Total Values: {len([r for r in analyzer.data if r.get(column)])}")
                        print(f"  Unique Values: {len(analyzer.get_unique_values(column))}")
                        print(f"  Most Common: {analyzer.get_mode(column)}")
                        print("=" * 50)
            
            elif choice == 5:
                column = get_column_choice("Select column to filter", analyzer)
                if column:
                    print("\nFilter options:")
                    print("1. Equals")
                    print("2. Greater than")
                    print("3. Less than")
                    print("4. Contains")
                    print("5. Between")
                    
                    try:
                        filter_choice = int(input("Select filter (1-5): "))
                        
                        if filter_choice == 1:
                            value = input(f"Enter value to match: ")
                            filtered = analyzer.filter_equals(column, value)
                        elif filter_choice == 2:
                            value = float(input(f"Enter minimum value: "))
                            filtered = analyzer.filter_greater_than(column, value)
                        elif filter_choice == 3:
                            value = float(input(f"Enter maximum value: "))
                            filtered = analyzer.filter_less_than(column, value)
                        elif filter_choice == 4:
                            substring = input(f"Enter substring to search for: ")
                            filtered = analyzer.filter_contains(column, substring)
                        elif filter_choice == 5:
                            min_val = float(input(f"Enter minimum value: "))
                            max_val = float(input(f"Enter maximum value: "))
                            filtered = analyzer.filter_between(column, min_val, max_val)
                        else:
                            print("Invalid choice.")
                            filtered = []
                        
                        print(f"\nFiltered to {len(filtered)} records")
                        
                        view = input("View filtered data? (y/n): ").lower()
                        if view == 'y':
                            analyzer.data = filtered
                            analyzer.display_data(10)
                        else:
                            print("Filter not applied to data.")
                    
                    except ValueError:
                        print("Invalid input.")
            
            elif choice == 6:
                column = get_column_choice("Select column to sort by", analyzer)
                if column:
                    reverse = input("Sort descending? (y/n): ").lower() == 'y'
                    if analyzer.sort_by_column(column, reverse):
                        print(f"Data sorted by {column} ({'descending' if reverse else 'ascending'})")
            
            elif choice == 7:
                column = get_column_choice("Select column", analyzer)
                if column:
                    try:
                        bins = int(input("Enter number of bins (default 10): ") or "10")
                        analyzer.display_histogram(column, bins)
                    except ValueError:
                        analyzer.display_histogram(column)
            
            elif choice == 8:
                column = get_column_choice("Select column", analyzer)
                if column:
                    try:
                        top_n = int(input("Top N items (default 20): ") or "20")
                        analyzer.display_bar_chart(column, top_n)
                    except ValueError:
                        analyzer.display_bar_chart(column)
            
            elif choice == 9:
                if not analyzer.data:
                    print("No data loaded.")
                else:
                    print(analyzer.generate_summary_report())
                    
                    save = input("\nSave report to file? (y/n): ").lower()
                    if save == 'y':
                        filename = input("Enter filename (default 'report.txt'): ").strip() or "report.txt"
                        analyzer.save_report(filename)
            
            elif choice == 10:
                if not analyzer.data:
                    print("No data to export.")
                else:
                    filename = input("Enter CSV filename (default 'output.csv'): ").strip() or "output.csv"
                    analyzer.export_to_csv(filename)
            
            elif choice == 11:
                if not analyzer.data:
                    print("No data to export.")
                else:
                    filename = input("Enter JSON filename (default 'output.json'): ").strip() or "output.json"
                    analyzer.export_to_json(filename)
            
            elif choice == 12:
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 12.")
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()