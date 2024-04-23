class InterfaceMonitor:
    def __init__(self):
        self.last_read = self.last_write = -1
        self.read_sum = self.write_sum = self.read_count = self.write_count = self.bytes_transferred = 0

    def add_transaction(self, timestamp, txn_type, data):
        if txn_type == "Rd" and self.last_read != -1:
            self.read_sum += timestamp - self.last_read
            self.read_count += 1
        elif txn_type == "Wr" and self.last_write != -1:
            self.write_sum += timestamp - self.last_write
            self.write_count += 1
        elif txn_type == "Data":
            self.bytes_transferred += 32  # Assuming 32B per transfer

        if txn_type == "Rd":
            self.last_read = timestamp
        elif txn_type == "Wr":
            self.last_write = timestamp

    def calculate_latency_bandwidth(self):
        average_read_latency = self.read_sum / self.read_count if self.read_count > 0 else 0
        average_write_latency = self.write_sum / self.write_count if self.write_count > 0 else 0
        average_bandwidth = self.bytes_transferred / (self.read_count + self.write_count) if (self.read_count + self.write_count) > 0 else 0

        return average_read_latency, average_write_latency, average_bandwidth


# Example usage:
interface_monitor = InterfaceMonitor()

# Assuming monitor output is provided as shown in Table 1.0
interface_monitor.add_transaction(0, "Rd", "Addr1")
interface_monitor.add_transaction(2, "Wr", "Addr2")
interface_monitor.add_transaction(4, "Wr", "Addr3")
interface_monitor.add_transaction(10, "Data", "Addr1")

average_read_latency, average_write_latency, average_bandwidth = interface_monitor.calculate_latency_bandwidth()
print("Average Read Latency:", average_read_latency)
print("Average Write Latency:", average_write_latency)
print("Average Bandwidth:", average_bandwidth)
