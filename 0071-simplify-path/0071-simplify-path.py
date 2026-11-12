class Solution:
    def simplifyPath(self, path: str) -> str:
        #directory stack and .,/ stack
        stack=[]
        new_path=path.split('/')
        # print(new_path)
        for dirs in new_path:
            # print(dirs)
            if dirs=="" or dirs=='.':
                continue
            elif  dirs=="..":
                
                if stack:
                    stack.pop()
            else:
                stack+=[dirs]
                # stack+=['/']
            
            # print(stack)
        # print("".join(stack))
        # while len(stack)>1 and stack[-1]=='/':
        #     stack.pop()
        return "/"+"/".join(stack)

        