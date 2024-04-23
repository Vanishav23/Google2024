# OptiNoC: Maximizing NoC Performance with RL
## Interface Monitor

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

CLASS InterfaceMonitor:
    METHOD __init__():
        Initialize last_read, last_write, read_sum, write_sum, read_count, write_count, bytes_transferred to -1, 0, 0, 0, 0, 0, 0

    METHOD add_transaction(timestamp, txn_type, data):
        IF txn_type is "Rd" AND last_read is not -1:
            Increment read_sum by (timestamp - last_read) and increment read_count by 1
        ELSE IF txn_type is "Wr" AND last_write is not -1:
            Increment write_sum by (timestamp - last_write) and increment write_count by 1
        ELSE IF txn_type is "Data":
            Increment bytes_transferred by 32

        IF txn_type is "Rd": Set last_read to timestamp
        ELSE IF txn_type is "Wr": Set last_write to timestamp

    METHOD calculate_latency_bandwidth():
        Compute average_read_latency as read_sum / read_count if read_count > 0, otherwise set to 0
        Compute average_write_latency as write_sum / write_count if write_count > 0, otherwise set to 0
        Compute average_bandwidth as bytes_transferred / (read_count + write_count) if (read_count + write_count) > 0, otherwise set to 0
        RETURN average_read_latency, average_write_latency, average_bandwidth

    CREATE interface_monitor as new InterfaceMonitor()
    FOR EACH transaction in [("Rd", 0), ("Wr", 2), ("Wr", 4), ("Data", 10)]:
    CALL add_transaction(transaction[1], transaction[0], "Addr" + str(transaction[1] + 1)) on interface_monitor

    CALL calculate_latency_bandwidth() on interface_monitor and STORE results in average_read_latency, average_write_latency, average_bandwidth
    DISPLAY "Average Read Latency:", average_read_latency, "Average Write Latency:", average_write_latency, "Average Bandwidth:", average_bandwidth

3. **View Results**: The script will run and output the average read latency, average write latency, and average bandwidth based on the transactions provided in the example usage section.

## Example Usage

from interface_monitor import InterfaceMonitor

Create an instance of the InterfaceMonitor class
interface_monitor = InterfaceMonitor()

Add transactions to the interface monitor
interface_monitor.add_transaction(0, "Rd", "Addr1")
interface_monitor.add_transaction(2, "Wr", "Addr2")
interface_monitor.add_transaction(4, "Wr", "Addr3")
interface_monitor.add_transaction(10, "Data", "Addr1")

Calculate average read latency, average write latency, and average bandwidth
average_read_latency, average_write_latency, average_bandwidth = interface_monitor.calculate_latency_bandwidth()

Print the results
print("Average Read Latency:", average_read_latency)
print("Average Write Latency:", average_write_latency)
print("Average Bandwidth:", average_bandwidth)

## Additional Information
The add_transaction method is used to add transactions to the interface monitor. It takes three arguments: timestamp, txn_type, and data.<br/>
timestamp: The time at which the transaction occurred.<br/>
txn_type: The type of transaction, which can be "Rd" (read), "Wr" (write), or "Data" (data transfer).<br/>
data: Additional data associated with the transaction.<br/>
The calculate_latency_bandwidth method calculates the average read latency, average write latency, and average bandwidth based on the transactions added using add_transaction.<br/>
The average read latency is the average time between successive read transactions.<br/>
The average write latency is the average time between successive write transactions.<br/>
The average bandwidth is the average amount of data transferred per transaction (assuming 32 bytes per transfer).<br/>
