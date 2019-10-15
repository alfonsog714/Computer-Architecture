"""CPU functionality."""

import sys

HALT = 1
SAVE = 130
PRINT = 71


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.pc = 0
        self.ram = [0] * 2048  # 256 or 2048?
        self.registers = [0] * 8

    def load(self):
        """Load a program into memory."""

        address = 0

        if len(sys.argv) != 2:
            print("Usage: file.py <filename>", file=sys.stderr)
            sys.exit(1)

        try:
            with open(sys.argv[1]) as f:
                for line in f:
                    # print(line)

                    # Ignore anything after a #
                    comment_split = line.split("#")

                    # Convert any numbers from binary strings to integers
                    num = comment_split[0]
                    try:
                        x = int(num, 2)
                        print(x)
                    except ValueError:
                        continue

        except FileNotFoundError:
            print(f"{sys.argv[0]}: {sys.argv[1]} not found.")
            sys.exit(2)

        # for instruction in range(2):
        #     self.ram[address] = instruction
        #     address += 1

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value
        return self.ram[address]

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True

        while running:
            command = self.ram[self.pc]

            if command == HALT:
                running = False
                self.pc += 1

            elif command == SAVE:
                reg = self.ram[self.pc + 1]
                value = self.ram[self.pc + 2]
                self.registers[reg] = value
                self.pc += 3

            elif command == PRINT:
                reg = self.ram[self.pc + 1]
                print(self.registers[reg])
                self.pc += 2

            else:
                print(f"Unkown instruction: {command}")
                sys.exit(1)
