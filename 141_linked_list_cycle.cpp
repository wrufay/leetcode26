// 141. Linked List Cycle
// First solved 05/03/26

 struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};
 
class Solution {
    public:
        bool hasCycle(ListNode *head) {

            // fast/slow method: if there's a cycle in the list, eventually
            // fast and slow will be the same node. otherwise if fast reaches
            // null, that means there's no cycle
            ListNode *fast = head;
            ListNode *slow = head;
    
            while(fast && fast->next) {
                fast = fast->next->next;
                slow = slow->next;
                if(fast == slow) {
                    return true;
                }
            }
            return false;
        }
    };