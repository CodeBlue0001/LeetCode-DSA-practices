class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1_x1=rec1[0]
        rec1_x2=rec1[2]
        rec1_y1=rec1[1]
        rec1_y2=rec1[3]

        rec2_x1=rec2[0]
        rec2_x2=rec2[2]
        rec2_y1=rec2[1]
        rec2_y2=rec2[3]

        x_overlap=rec1_x1<rec2_x2 and rec1_x2>rec2_x1
        y_overlap=rec1_y1<rec2_y2 and rec1_y2>rec2_y1
        
        return x_overlap and y_overlap