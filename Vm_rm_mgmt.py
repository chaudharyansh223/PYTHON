class VirtualMachine:
    def __init__(self,vm_name,total_rm_db):
        self.vm_name = vm_name
        self.total_rm_gb = total_rm_db
        self.used_rm_gb = 0
    def allocate(self, amount_gb):
        total_used_rm_gb = amount_gb + self.used_rm_gb
        if total_used_rm_gb > self.total_rm_gb:
            print("insufficient rm")
        else:
            print(f"allocated {amount_gb}GB")
            self.used_rm_gb+= amount_gb
    def deallocate(self,amount_gb):
        if  amount_gb < self.used_rm_gb:
            print(f"deallocat {amount_gb}GB")
            self.used_rm_gb-= amount_gb
    def allocated_rm(self):
        available_rm = self.total_rm_gb - self.used_rm_gb
        print(available_rm)
Vm1 = VirtualMachine("linux",16)
Vm1.allocate(10)
Vm1.allocated_rm()
Vm1.deallocate(4)
Vm1.allocated_rm()

    


