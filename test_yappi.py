import yappi
from test_func_cpu_1 import func_1

yappi.set_clock_type("cpu") # Use set_clock_type("wall") for wall time
yappi.start()
func_1(10)

yappi.get_func_stats().print_all()
yappi.get_thread_stats().print_all()
