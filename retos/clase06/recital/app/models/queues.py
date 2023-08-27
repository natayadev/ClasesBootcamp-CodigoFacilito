""" Queues Model for Recital """
# __doc__ (Queues Model file for little Recital app for testing
# Queues and Piles)


class QueueData():
    """
    Class for Ramdom Data Model

    Arguments:
    lang (object)
    data (list)
    search (int)

    Returns a orderer ramdom list from 3 optional modes.

    >>> queues = QueueData()
    >>> queues.queue_list
    []

    TODO:
        -

    """

    _pit_list = []
    _queue_list = []
    _capacity = 10

    def __init__(self, pit_list: list, queue_list: list,
                 lang: object, cfg: object) -> object:
        """
        Init Function

        Arguments:
        self
        """
        self.lang = lang
        self._capacity = cfg.getint("OPTIONS", "STAGE_CAPACITY")

        self._pit_list = self.list_complete(
            pit_list, self.lang["LANG"]["LANG_INPUT_FREE_SEAT"],
            self._capacity)

        self._queue_list = self.list_complete(
            queue_list, self.lang["LANG"]["LANG_INPUT_FREE_QUEUE"],
            self._capacity)

    @property
    def pit_list(self) -> list:
        """
        Property Getter for pit list

        Arguments:
        self

        Returns getter of pit_list for data builder (list)

        >>> self.pit_list
        []

        TODO:
            -
        """
        return self._pit_list

    @pit_list.setter
    def pit_list(self, value: str) -> list:
        """
        Function Setter for pit list

        Arguments:
        self
        value (str)

        Returns setter for pit_list to select data builder (list)

        >>> queues = QueueData()
        >>> queues.pit_list
        []

        TODO:
            -
        """
        self._pit_list = value

    @property
    def queue_list(self) -> list:
        """
        Property Getter for queue list

        Arguments:
        self

        Returns getter of pit_list for data builder (list)

        >>> self.queue_list
        []

        TODO:
            -
        """
        return self._queue_list

    @queue_list.setter
    def queue_list(self, value: str) -> list:
        """
        Function Setter for queue list

        Arguments:
        self
        value (str)

        Returns setter for queue_list to select data builder (list)

        >>> queue = QueueData()
        >>> queue.queue_list
        []

        TODO:
            -
        """
        self._queue_list = value

    def list_empty(self, current_list, default_empty):
        """
        Function to check if a list is empty

        Arguments:
        self
        current_list (list)
        default_empty (str)

        Returns True is the list is empty (removes the default
        free queues or seats) (boolean)

        >>> queue = QueueData()
        >>> queue.list_empty(curr_list[], "FREE QUEUE")
        True

        TODO:
            -
        """
        temp_list = current_list.copy()
        self.list_iterate(temp_list, default_empty, mode='drop')
        return len(temp_list) == 0

    def list_full(self, current_list, default_empty):
        """
        Function to check if a list is full

        Arguments:
        self
        current_list (list)
        default_empty (str)

        Returns True is the list is full (removes the default free
        queues or seats) (boolean)

        >>> queue = QueueData()
        >>> queue.list_full(curr_list[], "FREE QUEUE")
        True

        TODO:
            -
        """
        temp_list = current_list.copy()
        self.list_iterate(temp_list, default_empty, mode='drop')
        return len(temp_list) == self._capacity

    def list_top(self, current_list, default_empty):
        """
        Function to get the top value of the list

        Arguments:
        self
        current_list (list)
        default_empty (str)

        Returns the top value of the list (str)

        >>> queue = QueueData()
        >>> queue.list_top(curr_list[], "FREE QUEUE")
        curr_list[0]

        TODO:
            -
        """
        if self.list_empty(current_list, default_empty):
            return None

        return current_list[0]

    def list_add(self, current_list, default_empty, element):
        """
        Function to add a value in to the list

        Arguments:
        self
        current_list (list)
        default_empty (str)
        element (str)

        Returns to add a value in to the list (reorders the
        default free queues or seats)  (str)

        >>> queue = QueueData()
        >>> queue.list_add(curr_list[], "FREE QUEUE", "Gonzalo")
        []

        TODO:
            -
        """
        if self.list_full(current_list, default_empty):
            return None

        current_list.pop(-1)
        current_list.append(element)
        return self.list_iterate(current_list, default_empty, 'reorder')

    def list_complete(self, current_list, default_empty, capacity):
        """
        Function to complete the lists with reorder

        Arguments:
        self
        current_list (list)
        default_empty (str)

        Returns a complete list with default free
        queues or seats, limited by capacity (list)

        >>> queue = QueueData()
        >>> queue.list_complete(curr_list[], "FREE QUEUE", 10)
        []

        TODO:
            -
        """
        while len(current_list) < capacity:
            current_list.append(default_empty)
        return current_list

    def list_iterate(self, current_list, default_empty, mode='reorder'):
        """
        Function to iterate with a reorder or drops, returns a list

        Arguments:
        self
        current_list (list)
        default_empty (str)

        Returns a list with orderer default free
        queues or seats, or a clean list without
        default free queues or seats (list)

        >>> queue = QueueData()
        >>> queue.list_iterate(curr_list[], "FREE QUEUE", 'reorder/drop')
        []

        TODO:
            -
        """
        counter = 0
        end = len(current_list) - 1

        while counter <= end:
            if current_list[counter] == default_empty:
                if mode == 'reorder':
                    current_list.append(current_list.pop(counter))

                if mode == 'drop':
                    current_list.pop(counter)
                end -= 1
            else:
                counter += 1
        return current_list

    def queue_to_pil(self, queue_list, default_empty_queue,
                     pil_list, default_empty_pil):
        """
        Function to moves the first index of the list, to another
        list in first index

        Arguments:
        self
        current_list (list)
        default_empty (str)

        Moves the first index of the list, to another list in first
        index, and (reorders the default free queues or seats) (list)

        >>> queue = QueueData()
        >>> queue.queue_to_pil(curr_list[], "FREE QUEUE",
        curr_pit_list[], "FREE SEAT")
        []

        TODO:
            -
        """
        if self.list_empty(queue_list, default_empty_queue):
            return None

        element_out = queue_list.pop(0)
        self.list_complete(queue_list, default_empty_queue, self._capacity)
        pil_list.pop(-1)
        pil_list.append(element_out)
        return self.list_iterate(pil_list, default_empty_pil, 'reorder')

    def pit_remove_generator(self, pit_list):
        """
        Function to make a lazy generator

        Arguments:
        self
        pit_list (list)

        Returns a generator where the elements of a list gets out,
        so finally we get an empty list (reorders the default free
        seats) (list)

        >>> queue = QueueData()
        >>> queue.pit_remove_generator(curr_pit_list[])
        []

        TODO:
            -
        """
        for pit in pit_list:
            if pit != self.lang["LANG"]["LANG_INPUT_FREE_SEAT"]:
                pit_list.remove(pit)
                pit_list.insert(0, self.lang["LANG"]["LANG_INPUT_FREE_SEAT"])
                yield input(
                    self.lang["LANG"]["LANG_INPUT_STAGE_PIL_OUT"].format(pit))
