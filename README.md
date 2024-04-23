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
## Brief Summary of the Solution

As per the problem, the pseudocode used to measure average latency and bandwidth can be written as follows:

class InterfaceMonitor:
    def __init__(self):
        # Initialize variables

    def add_transaction(self, timestamp, txn_type, data):
        # Add transaction details

    def calculate_latency_bandwidth(self):
        # Calculate average latency and bandwidth
3. **View Results**: The script will run and output the average read latency, average write latency, and average bandwidth based on the transactions provided in the example usage section.

## Example Usage

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

Additional Information
The add_transaction method is used to add transactions to the interface monitor. It takes three arguments: timestamp, txn_type, and data.
timestamp: The time at which the transaction occurred.
txn_type: The type of transaction, which can be "Rd" (read), "Wr" (write), or "Data" (data transfer).
data: Additional data associated with the transaction.
The calculate_latency_bandwidth method calculates the average read latency, average write latency, and average bandwidth based on the transactions added using add_transaction.
The average read latency is the average time between successive read transactions.
The average write latency is the average time between successive write transactions.
The average bandwidth is the average amount of data transferred per transaction (assuming 32 bytes per transfer).
