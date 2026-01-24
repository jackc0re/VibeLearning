# 🎯 Data Analyzer Challenges

Extend your data analyzer with these advanced features for professional data analysis.

---

## Challenge 1: Grouping and Aggregation

Add ability to group data by columns and calculate aggregate statistics.

### Features to Add

1. **Group By** — Group data by column value
2. **Aggregations** — Calculate aggregates for each group
3. **Multiple Groupings** — Group by multiple columns
4. **Custom Aggregations** — Add custom aggregation functions

### Implementation

```python
class DataAnalyzer:
    def group_by(self, column):
        """Group data by column value."""
        groups = {}
        
        for row in self.data:
            key = row.get(column)
            if key not in groups:
                groups[key] = []
            groups[key].append(row)
        
        return groups
    
    def aggregate_group(self, group, column, aggregation='sum'):
        """Calculate aggregation for a group on a column."""
        values = [float(row.get(column, 0)) for row in group]
        
        if aggregation == 'sum':
            return sum(values)
        elif aggregation == 'mean':
            return sum(values) / len(values) if values else 0
        elif aggregation == 'count':
            return len(values)
        elif aggregation == 'min':
            return min(values) if values else 0
        elif aggregation == 'max':
            return max(values) if values else 0
    
    def group_by_aggregate(self, group_column, value_column, aggregation='sum'):
        """Group by column and calculate aggregation."""
        groups = self.group_by(group_column)
        
        results = []
        for key, group in groups.items():
            result = {
                group_column: key,
                aggregation: self.aggregate_group(group, value_column, aggregation),
                'count': len(group)
            }
            results.append(result)
        
        return sorted(results, key=lambda x: x[aggregation], reverse=True)
    
    def display_grouped_results(self, group_column, value_column, aggregation='sum'):
        """Display grouped results in a table."""
        results = self.group_by_aggregate(group_column, value_column, aggregation)
        
        print(f"\nGrouped by {group_column}, Aggregation: {aggregation}")
        print("=" * 60)
        print(f"{group_column:20s} | {aggregation:10s} | Count")
        print("-" * 60)
        
        for result in results:
            print(f"{str(result[group_column]):20s} | {result[aggregation]:10.2f} | {result['count']:5d}")
        
        print("=" * 60)
```

---

## Challenge 2: Pivot Tables

Create pivot table functionality for cross-tabulation.

### Features to Add

1. **Create Pivot** — Create cross-tabulation of two columns
2. **Value Aggregation** — Choose aggregation function
3. **Row/column Totals** — Add totals to pivot tables
4. **Multiple Values** — Support multiple value columns

### Implementation

```python
class DataAnalyzer:
    def create_pivot(self, row_column, col_column, value_column, aggregation='sum'):
        """Create a pivot table."""
        row_values = self.get_unique_values(row_column)
        col_values = self.get_unique_values(col_column)
        
        pivot = {
            'rows': row_column,
            'columns': col_column,
            'row_values': row_values,
            'col_values': col_values,
            'data': {},
            'col_totals': {},
            'row_totals': {},
            'grand_total': 0
        }
        
        for row_val in row_values:
            pivot['data'][row_val] = {}
            pivot['row_totals'][row_val] = 0
            
            for col_val in col_values:
                filtered = [r for r in self.data 
                           if r.get(row_column) == row_val and r.get(col_column) == col_val]
                
                if filtered:
                    values = [float(r.get(value_column, 0)) for r in filtered]
                    
                    if aggregation == 'sum':
                        aggregation_value = sum(values)
                    elif aggregation == 'mean':
                        aggregation_value = sum(values) / len(values) if values else 0
                    elif aggregation == 'count':
                        aggregation_value = len(values)
                    else:
                        aggregation_value = sum(values)
                else:
                    aggregation_value = 0
                
                pivot['data'][row_val][col_val] = aggregation_value
                pivot['row_totals'][row_val] += aggregation_value
                
                pivot['col_totals'][col_val] = pivot['col_totals'].get(col_val, 0) + aggregation_value
                pivot['grand_total'] += aggregation_value
        
        return pivot
    
    def display_pivot(self, pivot):
        """Display pivot table."""
        print(f"\nPivot Table: Rows by {pivot['rows']}, Columns by {pivot['columns']}")
        print("=" * 80)
        
        headers = [''] + pivot['col_values'] + ['Row Total']
        header_row = ' | '.join(f"{h:12s}" for h in headers)
        print(header_row)
        print("-" * 80)
        
        for row_val in pivot['row_values']:
            row = [row_val] + \
                  [pivot['data'][row_val].get(col_val, 0) for col_val in pivot['col_values']] + \
                  [pivot['row_totals'][row_val]]
            
            row_str = ' | '.join(f"{str(v):12s}" for v in row)
            print(row_str)
        
        col_totals = ['Column Total'] + \
                    [pivot['col_totals'].get(col_val, 0) for col_val in pivot['col_values']] + \
                    [pivot['grand_total']]
        
        total_str = ' | '.join(f"{str(v):12s}" for v in col_totals)
        print(total_str)
        print("=" * 80)
```

---

## Challenge 3: Data Cleaning

Add data cleaning capabilities for handling missing values and outliers.

### Features to Add

1. **Detect Missing Values** — Find and count missing values
2. **Fill Missing Values** — Fill with mean, median, or custom value
3. **Remove Rows with Missing** — Drop incomplete records
4. **Detect Outliers** — Identify statistical outliers
5. **Handle Outliers** — Remove or cap outliers

### Implementation

```python
class DataAnalyzer:
    def detect_missing_values(self):
        """Detect missing values in the dataset."""
        missing_report = {}
        
        for column in self.headers:
            missing_count = sum(1 for row in self.data 
                              if row.get(column) is None or row.get(column) == '')
            missing_report[column] = {
                'count': missing_count,
                'percentage': (missing_count / len(self.data)) * 100 if self.data else 0
            }
        
        return missing_report
    
    def fill_missing_values(self, column, method='mean'):
        """Fill missing values with specified method."""
        if not self.is_numeric_column(column):
            print(f"Column '{column}' is not numeric")
            return False
        
        filled = 0
        
        if method == 'mean':
            values = self.get_numeric_values(column)
            fill_value = sum(values) / len(values) if values else 0
        elif method == 'median':
            values = self.get_numeric_values(column)
            fill_value = median(values) if values else 0
        elif method == 'mode':
            fill_value = self.get_mode(column) or 0
        else:
            fill_value = method
        
        for i, row in enumerate(self.data):
            if row.get(column) is None or row.get(column) == '':
                self.data[i][column] = fill_value
                filled += 1
        
        return filled
    
    def detect_outliers(self, column, method='iqr'):
        """Detect outliers in a numeric column."""
        if not self.is_numeric_column(column):
            return []
        
        values = self.get_numeric_values(column)
        
        if method == 'iqr':
            q1 = self.calculate_percentile(sorted(values), 25)
            q3 = self.calculate_percentile(sorted(values), 75)
            iqr = q3 - q1
            
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
        
        elif method == 'zscore':
            mean_val = sum(values) / len(values)
            std_dev = self.calculate_std_dev(values)
            
            lower_bound = mean_val - 3 * std_dev
            upper_bound = mean_val + 3 * std_dev
        
        else:
            return []
        
        outliers = []
        for row in self.data:
            value = float(row.get(column, 0))
            if value < lower_bound or value > upper_bound:
                outliers.append(row)
        
        return outliers
    
    def cap_outliers(self, column, method='iqr'):
        """Cap outliers at the bounds."""
        values = self.get_numeric_values(column)
        
        q1 = self.calculate_percentile(sorted(values), 25)
        q3 = self.calculate_percentile(sorted(values), 75)
        iqr = q3 - q1
        
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        capped = 0
        for row in self.data:
            value = float(row.get(column, 0))
            if value < lower_bound:
                row[column] = lower_bound
                capped += 1
            elif value > upper_bound:
                row[column] = upper_bound
                capped += 1
        
        return capped
```

---

## Challenge 4: Correlation Analysis

Add correlation analysis between numeric columns.

### Features to Add

1. **Pearson Correlation** — Calculate Pearson correlation coefficient
2. **Correlation Matrix** — Create matrix of all column correlations
3. **Correlation Heatmap** — Visual ASCII heatmap
4. **High Correlation Detection** — Find highly correlated columns

### Implementation

```python
class DataAnalyzer:
    def calculate_correlation(self, col1, col2):
        """Calculate Pearson correlation coefficient between two columns."""
        if not self.is_numeric_column(col1) or not self.is_numeric_column(col2):
            return None
        
        values1 = self.get_numeric_values(col1)
        values2 = self.get_numeric_values(col2)
        
        if len(values1) != len(values2):
            return None
        
        n = len(values1)
        if n < 2:
            return 0
        
        mean1 = sum(values1) / n
        mean2 = sum(values2) / n
        
        numerator = sum((v1 - mean1) * (v2 - mean2) for v1, v2 in zip(values1, values2))
        denominator1 = math.sqrt(sum((v1 - mean1) ** 2 for v1 in values1))
        denominator2 = math.sqrt(sum((v2 - mean2) ** 2 for v2 in values2))
        
        if denominator1 * denominator2 == 0:
            return 0
        
        return numerator / (denominator1 * denominator2)
    
    def correlation_matrix(self):
        """Create correlation matrix for all numeric columns."""
        numeric_columns = [col for col in self.headers if self.is_numeric_column(col)]
        
        matrix = {}
        for col1 in numeric_columns:
            matrix[col1] = {}
            for col2 in numeric_columns:
                matrix[col1][col2] = self.calculate_correlation(col1, col2)
        
        return matrix
    
    def display_correlation_heatmap(self, matrix=None):
        """Display correlation matrix as ASCII heatmap."""
        if matrix is None:
            matrix = self.correlation_matrix()
        
        numeric_columns = list(matrix.keys())
        
        print("\nCorrelation Heatmap")
        print("=" * 80)
        
        header = " " * 12 + " | ".join(f"{col:10s}" for col in numeric_columns)
        print(header)
        print("-" * 80)
        
        for col1 in numeric_columns:
            row = []
            for col2 in numeric_columns:
                corr = matrix[col1][col2]
                if corr is None:
                    value_str = "N/A      "
                else:
                    value_str = f"{corr:8.3f}"
                    if abs(corr) >= 0.8:
                        value_str = value_str + "█"
                    elif abs(corr) >= 0.6:
                        value_str = value_str + "▓"
                    elif abs(corr) >= 0.4:
                        value_str = value_str + "▒"
                    elif abs(corr) >= 0.2:
                        value_str = value_str + "░"
                    else:
                        value_str = value_str + " "
                row.append(value_str)
            
            row_str = f"{col1:12s} | " + " | ".join(row)
            print(row_str)
        
        print("=" * 80)
    
    def find_high_correlations(self, threshold=0.8):
        """Find column pairs with correlation above threshold."""
        matrix = self.correlation_matrix()
        high_corrs = []
        
        numeric_columns = list(matrix.keys())
        for i, col1 in enumerate(numeric_columns):
            for col2 in numeric_columns[i + 1:]:
                corr = matrix[col1][col2]
                if corr is not None and abs(corr) >= threshold:
                    high_corrs.append((col1, col2, corr))
        
        high_corrs.sort(key=lambda x: abs(x[2]), reverse=True)
        return high_corrs
```

---

## Challenge 5: Time Series Analysis

Add functionality to work with date/time data.

### Features to Add

1. **Date Parsing** — Parse various date formats
2. **Time Grouping** — Group by day, week, month, year
3. **Trend Analysis** — Calculate trends over time
4. **Rolling Averages** — Compute moving averages
5. **Time-based Aggregations** — Aggregate by time periods

### Implementation

```python
from datetime import datetime, timedelta

class DataAnalyzer:
    def parse_date(self, date_str, format_str=None):
        """Parse date string with auto-detection or specified format."""
        if not date_str:
            return None
        
        formats = [
            '%Y-%m-%d',
            '%Y/%m/%d',
            '%d-%m-%Y',
            '%d/%m/%Y',
            '%m/%d/%Y',
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%dT%H:%M:%S'
        ]
        
        if format_str:
            formats.insert(0, format_str)
        
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        
        return None
    
    def group_by_time(self, date_column, period='day'):
        """Group data by time period."""
        groups = {}
        
        for row in self.data:
            date_val = row.get(date_column)
            if isinstance(date_val, str):
                date_obj = self.parse_date(date_val)
            elif isinstance(date_val, datetime):
                date_obj = date_val
            else:
                continue
            
            if period == 'day':
                key = date_obj.strftime('%Y-%m-%d')
            elif period == 'week':
                week_start = date_obj - timedelta(days=date_obj.weekday())
                key = week_start.strftime('%Y-W%W')
            elif period == 'month':
                key = date_obj.strftime('%Y-%m')
            elif period == 'year':
                key = date_obj.strftime('%Y')
            else:
                key = date_obj.strftime('%Y-%m-%d')
            
            if key not in groups:
                groups[key] = []
            groups[key].append(row)
        
        return groups
    
    def calculate_trend(self, date_column, value_column):
        """Calculate linear trend between date and value."""
        data_points = []
        
        for row in self.data:
            date_val = row.get(date_column)
            value_val = row.get(value_column)
            
            if isinstance(date_val, str):
                date_obj = self.parse_date(date_val)
            elif isinstance(date_val, datetime):
                date_obj = date_val
            else:
                continue
            
            try:
                value_float = float(value_val)
                timestamp = date_obj.timestamp()
                data_points.append((timestamp, value_float))
            except (ValueError, TypeError):
                continue
        
        if len(data_points) < 2:
            return None
        
        n = len(data_points)
        sum_x = sum(p[0] for p in data_points)
        sum_y = sum(p[1] for p in data_points)
        sum_xy = sum(p[0] * p[1] for p in data_points)
        sum_x2 = sum(p[0] ** 2 for p in data_points)
        
        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        intercept = (sum_y - slope * sum_x) / n
        
        return {
            'slope': slope,
            'intercept': intercept,
            'trend': 'increasing' if slope > 0 else 'decreasing'
        }
    
    def rolling_average(self, column, window_size=5):
        """Calculate rolling average."""
        values = self.get_numeric_values(column)
        
        if len(values) < window_size:
            return []
        
        rolling_averages = []
        
        for i in range(len(values) - window_size + 1):
            window = values[i:i + window_size]
            avg = sum(window) / window_size
            rolling_averages.append(avg)
        
        return rolling_averages
```

---

## Challenge 6: Advanced Filters

Add complex filtering capabilities.

### Features to Add

1. **Regular Expressions** — Filter using regex patterns
2. **Multiple Conditions** — Combine filters with AND/OR
3. **Custom Functions** — Use custom functions for filtering
4. **Filter Profiles** — Save and load filter configurations

### Implementation

```python
import re

class DataAnalyzer:
    def filter_regex(self, column, pattern, case_sensitive=False):
        """Filter using regular expression."""
        flags = 0 if case_sensitive else re.IGNORECASE
        
        try:
            compiled_pattern = re.compile(pattern, flags)
        except re.error as e:
            print(f"Invalid regex pattern: {e}")
            return []
        
        filtered = []
        for row in self.data:
            value = str(row.get(column, ''))
            if compiled_pattern.search(value):
                filtered.append(row)
        
        return filtered
    
    def filter_custom(self, filter_func):
        """Filter using custom function."""
        filtered = []
        
        for row in self.data:
            try:
                if filter_func(row):
                    filtered.append(row)
            except Exception as e:
                pass
        
        return filtered
    
    def filter_multiple(self, conditions, operator='AND'):
        """Apply multiple filter conditions."""
        if operator.upper() == 'AND':
            filtered = self.data
            for condition in conditions:
                filtered = self._apply_single_filter(filtered, condition)
                if not filtered:
                    break
        
        elif operator.upper() == 'OR':
            filtered = []
            for condition in conditions:
                result = self._apply_single_filter(self.data, condition)
                filtered.extend(result)
            
            filtered = list({tuple(row.items()) for row in [dict(t) for t in filtered]})
            filtered = [dict(t) for t in filtered]
        
        return filtered
    
    def _apply_single_filter(self, data, condition):
        """Apply a single filter condition."""
        column = condition.get('column')
        operation = condition.get('operation')
        value = condition.get('value')
        
        if operation == 'equals':
            return [row for row in data if row.get(column) == value]
        elif operation == 'greater_than':
            return [row for row in data if float(row.get(column, 0)) > value]
        elif operation == 'less_than':
            return [row for row in data if float(row.get(column, 0)) < value]
        elif operation == 'regex':
            pattern = value.get('pattern')
            case_sensitive = value.get('case_sensitive', False)
            if not case_sensitive:
                flags = re.IGNORECASE
            else:
                flags = 0
            
            try:
                compiled = re.compile(pattern, flags)
                return [row for row in data if compiled.search(str(row.get(column, '')))]
            except re.error:
                return []
        
        return data
```

---

## Challenge 7: Excel Support

Add support for reading Excel files with multiple sheets.

### Features to Add

1. **Read Excel Files** — Load data from .xlsx files
2. **Multiple Sheets** — Choose which sheet to load
3. **Sheet Listing** — List all sheets in workbook
4. **Cell Values** — Handle various cell value types

### Implementation

```python
# Requires: pip install openpyxl

def load_excel(self, filename, sheet_name=None):
    """Load data from Excel file."""
    try:
        from openpyxl import load_workbook
    except ImportError:
        print("openpyxl is required. Install with: pip install openpyxl")
        return False
    
    try:
        wb = load_workbook(filename, read_only=True)
        
        if sheet_name is None:
            print("\nAvailable sheets:")
            for i, sheet in enumerate(wb.sheetnames, 1):
                print(f"{i}. {sheet}")
            
            try:
                choice = int(input("Select sheet (number): ")) - 1
                sheet_name = wb.sheetnames[choice]
            except (ValueError, IndexError):
                print("Invalid choice. Using first sheet.")
                sheet_name = wb.sheetnames[0]
        
        ws = wb[sheet_name]
        
        self.headers = []
        data = []
        
        first_row = True
        for row in ws.iter_rows(values_only=True):
            if first_row:
                self.headers = [str(cell) if cell is not None else '' for cell in row]
                first_row = False
            else:
                row_dict = {}
                for i, cell in enumerate(row):
                    col_name = self.headers[i] if i < len(self.headers) else f'col_{i}'
                    row_dict[col_name] = cell
                data.append(row_dict)
        
        self.data = data
        self.filename = filename
        
        wb.close()
        print(f"Loaded {len(data)} records from '{sheet_name}' in {filename}")
        return True
    
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return False


def list_excel_sheets(self, filename):
    """List all sheets in an Excel file."""
    try:
        from openpyxl import load_workbook
    except ImportError:
        print("openpyxl is required.")
        return []
    
    try:
        wb = load_workbook(filename, read_only=True)
        sheets = wb.sheetnames
        wb.close()
        return sheets
    except Exception as e:
        print(f"Error listing sheets: {e}")
        return []
```

---

## Challenge 8: Data Validation

Add data validation and quality checks.

### Features to Add

1. **Type Validation** — Validate data types
2. **Range Validation** — Check values are within valid ranges
3. **Format Validation** — Validate data formats (dates, emails, etc.)
4. **Duplicate Detection** — Find duplicate records
5. **Validation Report** — Generate comprehensive validation report

### Implementation

```python
class DataAnalyzer:
    def validate_data_types(self, schema):
        """Validate data types according to schema."""
        errors = []
        
        for column, expected_type in schema.items():
            if column not in self.headers:
                errors.append(f"Column '{column}' not found")
                continue
            
            for row in self.data:
                value = row.get(column)
                
                if value is None or value == '':
                    continue
                
                if expected_type == 'numeric':
                    try:
                        float(value)
                    except (ValueError, TypeError):
                        errors.append(f"Row: {row} - Invalid numeric value in '{column}': {value}")
                
                elif expected_type == 'integer':
                    try:
                        int(value)
                    except (ValueError, TypeError):
                        errors.append(f"Row: {row} - Invalid integer value in '{column}': {value}")
                
                elif expected_type == 'date':
                    if self.parse_date(str(value)) is None:
                        errors.append(f"Row: {row} - Invalid date in '{column}': {value}")
        
        return errors
    
    def validate_ranges(self, column_ranges):
        """Validate values are within specified ranges."""
        errors = []
        
        for column, (min_val, max_val) in column_ranges.items():
            if column not in self.headers:
                continue
            
            for row in self.data:
                value = row.get(column)
                try:
                    numeric_value = float(value)
                    if numeric_value < min_val or numeric_value > max_val:
                        errors.append(f"Row: {row} - Value {numeric_value} in '{column}' outside range [{min_val}, {max_val}]")
                except (ValueError, TypeError):
                    pass
        
        return errors
    
    def find_duplicates(self, columns):
        """Find duplicate records based on specified columns."""
        seen = {}
        duplicates = []
        
        for row in self.data:
            key = tuple(str(row.get(col, '')) for col in columns)
            if key in seen:
                duplicates.append((seen[key], row))
            else:
                seen[key] = row
        
        return duplicates
    
    def generate_validation_report(self, schema, column_ranges=None, duplicate_cols=None):
        """Generate comprehensive validation report."""
        report = []
        report.append("=" * 80)
        report.append(" " * 25 + "DATA VALIDATION REPORT")
        report.append("=" * 80)
        
        type_errors = self.validate_data_types(schema)
        if type_errors:
            report.append(f"\nType Errors: {len(type_errors)}")
            for error in type_errors[:10]:
                report.append(f"  - {error}")
            if len(type_errors) > 10:
                report.append(f"  ... and {len(type_errors) - 10} more")
        
        if column_ranges:
            range_errors = self.validate_ranges(column_ranges)
            if range_errors:
                report.append(f"\nRange Errors: {len(range_errors)}")
                for error in range_errors[:10]:
                    report.append(f"  - {error}")
        
        if duplicate_cols:
            duplicates = self.find_duplicates(duplicate_cols)
            if duplicates:
                report.append(f"\nDuplicate Records: {len(duplicates)}")
                for dup in duplicates[:5]:
                    report.append(f"  - Duplicate based on {duplicate_cols}")
        
        report.append("=" * 80)
        
        return '\n'.join(report)
```

---

## 🏆 Challenge Completion

Track your progress:

- [ ] Challenge 1: Grouping and Aggregation
- [ ] Challenge 2: Pivot Tables
- [ ] Challenge 3: Data Cleaning
- [ ] Challenge 4: Correlation Analysis
- [ ] Challenge 5: Time Series Analysis
- [ ] Challenge 6: Advanced Filters
- [ ] Challenge 7: Excel Support
- [ ] Challenge 8: Data Validation

---

**Tip:** These challenges use advanced data analysis concepts. Each one builds valuable skills for data science and analytics!