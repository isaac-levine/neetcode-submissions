class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Create a dictionary to store the last occurrence of each character
        last_occurrence = {c: i for i, c in enumerate(s)}
        
        # Step 2: Initialize variables
        partitions = []
        start = end = 0
        
        # Step 3: Iterate through the string to determine the partitions
        for i, c in enumerate(s):
            # Update the end to the farthest last occurrence of the character
            end = max(end, last_occurrence[c])
            
            # If the current index is the end of the partition
            if i == end:
                # Append the size of the partition
                partitions.append(end - start + 1)
                # Move the start to the next character
                start = i + 1
        
        return partitions