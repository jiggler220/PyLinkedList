import unittest

from colorama import init, Fore

from linkedList import initLinkedList, hasCycle


def printColoredResult(result, expected):
    """
    Print the result in color based on if result is what is expected.
    """
    if result == expected:
        return Fore.GREEN + "SUCCESS"

    return Fore.RED + "FAIL"


class LinkedListCycleTest(unittest.TestCase):

    def testNonCyclic(self):
        """
        Test Non Cyclic Linked List
        """
        expectedResult = False

        # Create a linked list without a cycle
        linkedListWithoutCycle = initLinkedList([1, 2, 3, 4, 5])
        cyclic = hasCycle(linkedListWithoutCycle)
        print("Linked List without Cycle has a cycle:", printColoredResult(cyclic, expectedResult))
        self.assertEqual(hasCycle(linkedListWithoutCycle), expectedResult)

    def testCyclic(self):
        """
        Test Cyclic Linked List
        """

        expectedResult = True

        # Create a linked list with a cycle
        linkedListWithCycle = initLinkedList([1, 2, 3, 4, 5])

        # Create a cycle by connecting the last node to the second node
        current = linkedListWithCycle
        while current.next:
            current = current.next
        current.next = linkedListWithCycle.next
        cyclic = hasCycle(linkedListWithCycle)
        print("Linked List with Cycle has a cycle:", printColoredResult(cyclic, expectedResult))
        self.assertEqual(cyclic, expectedResult)


if __name__ == '__main__':

    # Initialize colorama to work on Windows as well
    init(autoreset=True)

    unittest.main()
