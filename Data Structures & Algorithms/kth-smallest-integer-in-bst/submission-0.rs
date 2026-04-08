// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//     pub val: i32,
//     pub left: Option<Rc<RefCell<TreeNode>>>,
//     pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         TreeNode {
//             val,
//             left: None,
//             right: None,
//         }
//     }
// }

use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    pub fn kth_smallest(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
        let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
        let mut curr = root;
        let mut k = k;

        loop {
            // go to the left-most node
            while let Some(node) = curr {
                curr = node.borrow().left.clone();
                stack.push(node);
            }
            if let Some(node) = stack.pop() {
                k-=1; // when k == 0, means we find all the elements before, so this is the one we want
                if k == 0 {
                    return node.borrow().val;
                }
                curr = node.borrow().right.clone();
            } else {
                break;
            }
        }

        -1
    }
}
