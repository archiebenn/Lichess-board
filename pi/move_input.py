import queue
import threading

class MoveInputHandler:
    """
    Manages move inputs from CLI and (eventually) from hall sensors in physical board.
    Uses a queue so moves can be collected without blocking game loop.
    """

    def __init__(self):
        self.move_queue = queue.Queue()
        self.input_thread = None
        self.stop_event = threading.Event()

    def start_cli_input(self):
        """
        Starts a separate thread to handle CLI input for moves, so it doesn't block the main game loop.
        """
        self.stop_event.clear()
        self.input_thread = threading.Thread(
            target=self.cli_input_loop, daemon=True
            )
        self.input_thread.start()

    def cli_input_loop(self):
        """
        Continuously reads CLI input and adds moves to the queue.   
        """
        while not self.stop_event.is_set():
            try:
                move = input("Enter move (e.g e2e4 format):").strip().lower()
                # 4 for standard e2e4, 5 for promotion case 
                if move and len(move) == 4 or 5:
                    self.move_queue.put(move)
            except EOFError:
                break


    def hall_sensor_input(self):
        """
        Placeholder for hall effect sensor loop
        """
        pass

    def get_move(self, timeout=None):
        """
        Blocking - waits for next move from queue with optional timeout and returns None if timeout expires
        """
        try:
            return self.move_queue.get(timeout=timeout)
        except queue.Empty:
            return None
        
    def stop(self):
        """
        Stop all input listening
        """
        self.stop_event.set()
        if self.input_thread and self.input_thread.is_alive():
            self.input_thread.join()
        

    