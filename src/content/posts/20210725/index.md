---
title: "php - Add Two Numbers"
subtitle: "php - Add Two Numbers"
date: 2021-07-25T17:23:13Z
tags:
  - "php"
  - "LeetCode"
---

今天用php來改寫吧!
Let's Go!!!

題目為  
```

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
```

### Example 1 :
![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

### Example 2 :
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

### Example 3 :
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

### 解法
---
1. 實際解法
    ``` php
    /**
    * Definition for a singly-linked list.
    * class ListNode {
    *     public $val = 0;
    *     public $next = null;
    *     function __construct($val = 0, $next = null) {
    *         $this->val = $val;
    *         $this->next = $next;
    *     }
    * }
    */
   class Solution {

    
       /**
        * @param ListNode $l1
        * @param ListNode $l2
        * @return ListNode
        */
       function addTwoNumbers($l1, $l2) {
           return  $this->calculation($l1,$l2,0);
       }
        
       
          /**
        * @param ListNode $l1
        * @param ListNode $l2
        * @param int $carry
        * @return ListNode
        */
       function calculation($l1, $l2 , $carry= 0) {
               if ($l1 == null && $l2 == null && $carry == 0) {
                    return null;
               }

           
               if ($l1 == null) {
                   $l1 = new ListNode(0, null);
               }

               if ($l2 == null) {
                   $l2 = new ListNode( 0,  null);
               }
           
               $val = $l1->val + $l2->val + $carry;
               $carry = intval(floor($val / 10));
           	return new ListNode($val % 10,$this->calculation($l1->next, $l2->next, $carry));
           }
       
   }
    ```

1. 執行效能
    ![](./img/php_performance.JPG)

碎碎念
===
沒想到 `php` 的效能也比 `C#` 好，但是也沒有贏過 `golang` ~~~
一樣都是遞迴寫法，沒想到差得比我想的還要多一點。
再來用 `TypeScript` 寫寫看囉!

