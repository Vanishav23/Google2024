# Interface Monitor

The Interface Monitor is a Python class designed to track read and write transactions on an interface and calculate average read latency, average write latency, and average bandwidth based on the recorded transactions.

## Environment Setup

1. **Python 3**: Ensure you have Python 3 installed on your system. You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone or download the repository containing the `interface_monitor.py` script.

## Running the Code

1. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory where the script is located.

2. **Execute the Script**: Run the following command to execute the code:

    ```bash
    python interface_monitor.py
    ```

3. **View Results**: The script will run and output the average read latency, average write latency, and average bandwidth based on the transactions provided in the example usage section.

## Example Usage

```python
from interface_monitor import InterfaceMonitor

# Create an instance of the InterfaceMonitor class
interface_monitor = InterfaceMonitor()

# Add transactions to the interface monitor
interface_monitor.add_transaction(0, "Rd", "Addr1")
interface_monitor.add_transaction(2, "Wr", "Addr2")
interface_monitor.add_transaction(4, "Wr", "Addr3")
interface_monitor.add_transaction(10, "Data", "Addr1")

# Calculate average read latency, average write latency, and average bandwidth
average_read_latency, average_write_latency, average_bandwidth = interface_monitor.calculate_latency_bandwidth()

# Print the results
print("Average Read Latency:", average_read_latency)
print("Average Write Latency:", average_write_latency)
print("Average Bandwidth:", average_bandwidth)
