class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left , right = 0, len(height)-1 # left , right 초깃값
        leftmax, rightmax, water = 0, 0, 0
        while left != right: #왼쪽 오른쪽 포인터가 같아질때까지
            leftmax = max(height[left], leftmax)#왼쪽최댓값
            rightmax = max(height[right], rightmax)#오른쪽최댓값
            if height[left] <= height[right]:#
                if height[left] < leftmax:#왼쪽최댓값보다 작으면
                    water += leftmax - height[left]#물을 최댓값의 차만큼 더함
                left += 1#한칸 이동
            elif height[left] > height[right]:
                if height[right] < rightmax:#오른쪽최댓값보다 작으면
                    water += rightmax - height[right]#물을 최댓값의 차만큼 더함
                right -=1#한칸 이동
                
        return water