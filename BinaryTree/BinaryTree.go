package main

//https://appliedgo.net/bintree/
import (
	"errors"
	"fmt"
	"log"
)

type Node struct {
	Value string
	Data  string
	Left  *Node
	Right *Node
}

func (n *Node) Insert(value, data string) error {
	if n == nil {
		return errors.New("Cannot insert value to a nil tree")
	}

	switch {
	case value == n.Value:
		return nil

	case value < n.Value:
		if n.Left == nil {
			n.Left = &Node{Value: value, Data: data}
			return nil
		}
		return n.Left.Insert(value, data)

	case value > n.Value:
		if n.Right == nil {
			n.Right = &Node{Value: value, Data: data}
			return nil
		}
		return n.Right.Insert(value, data)
	}
	return nil
}

func (n *Node) Find(s string) (string, bool) {
	if n == nil {
		return "", false
	}

	switch {
	case s == n.Value:
		return n.Data, true

	case s > n.Value:
		return n.Right.Find(s)

	default:
		return n.Left.Find(s)
	}
}

//findMax finds a maximum element in a sub-tree
func (n *Node) findMax(parent *Node) (*Node, *Node) {
	if n == nil {
		return nil, parent
	}
	//basement, a stop condition
	if n.Right == nil {
		return n, parent
	}
	//recursion
	return n.Right.findMax(n)
}

//replaceNode changes the parent's pointer to n by a pointer to replacement node
func (n *Node) replaceNode(parent, replacement *Node) error {
	if n == nil {
		return errors.New("replaceNode cannot work on a nil node")
	}

	if n == parent.Left {
		parent.Left = replacement
		return nil
	}

	parent.Right = replacement
	return nil
}

//Delete removes an element from the tree
func (n *Node) Delete(s string, parent *Node) error {
	//n is the node to be deleted
	if n == nil {
		return errors.New("node to be deleted does not exist in the tree")
	}

	switch {
	case s < n.Value:
		return n.Left.Delete(s, n)

	case s > n.Value:
		return n.Right.Delete(s, n)

	default:
		//n is a leaf
		if n.Left == nil && n.Right == nil {
			fmt.Println("n.Left == nil && n.Right == nil called, n.Value:", n.Value)
			n.replaceNode(parent, nil)
			return nil
		}
		if n.Left == nil {
			fmt.Println("n.Left == nil called, n.Value:", n.Value)
			n.replaceNode(parent, n.Right)
			return nil
		}
		if n.Right == nil {
			fmt.Println("n.Right == nil called, n.Value:", n.Value)
			n.replaceNode(parent, n.Left)
			return nil
		}
		replacement, replaceParent := n.Left.findMax(n)

		n.Value = replacement.Value
		n.Data = replacement.Data

		return replacement.Delete(replacement.Value, replaceParent)
	}
}

type Tree struct {
	Root *Node
}

func (t *Tree) Insert(value, data string) error {
	//add node if the root is empty
	if t.Root == nil {
		t.Root = &Node{Value: value, Data: data}
		return nil
	}
	return t.Root.Insert(value, data)
}

func (t *Tree) Find(s string) (string, bool) {
	//return nil if root is empty
	if t.Root == nil {
		return "", false
	}
	return t.Root.Find(s)
}

func (t *Tree) Delete(s string) error {
	if t.Root == nil {
		return errors.New("Cannot delete from an empty tree")
	}
	fakeParent := &Node{Right: t.Root}
	err := t.Root.Delete(s, fakeParent)
	if err != nil {
		return err
	}
	//if the root is deleted and it is the unique node in the tree
	if fakeParent.Right == nil {
		t.Root = nil
	}
	return nil
}

//TraverseIn goes through the tree in order (from left to right, small to large)
func (t *Tree) TraverseIn(n *Node, f func(*Node)) {
	if n == nil {
		return
	}
	t.TraverseIn(n.Left, f)
	f(n)
	t.TraverseIn(n.Right, f)
}

//TraversePre goes through the tree in pre order
func (t *Tree) TraversePre(n *Node, f func(*Node)) {
	if n == nil {
		return
	}
	f(n)
	t.TraversePre(n.Left, f)
	t.TraversePre(n.Right, f)
}

//TraversePost goes through the tree in post order
func (t *Tree) TraversePost(n *Node, f func(*Node)) {
	if n == nil {
		return
	}
	t.TraversePost(n.Left, f)
	t.TraversePost(n.Right, f)
	f(n)
}
func main() {
	//set up a slice of strings
	values := []string{"d", "b", "c", "e", "a"}
	data := []string{"demand", "bus", "cantie", "email", "apple"}
	tree := &Tree{}

	//insert values
	for i := 0; i < len(values); i++ {
		err := tree.Insert(values[i], data[i])
		if err != nil {
			log.Fatal("Value inserting error: ", values[i], " : ", err)
		}
	}

	//print tree
	fmt.Print("Sorted values: | ")
	tree.TraversePre(tree.Root, func(n *Node) { fmt.Print(n.Value, ": ", n.Data, " | ") })
	fmt.Println()

	//find value
	s := "a"
	fmt.Print("Finde node '", s, "': ")
	d, found := tree.Find(s)
	if !found {
		log.Fatal("Cannot find '" + s + "'")
	}
	fmt.Println("Found " + s + ": '" + d + "'")

	//delete value
	err := tree.Delete(s)
	if err != nil {
		log.Fatal("Error deleting "+s+": ", err)
	}
	fmt.Println("After deleting '" + s + "': ")
	tree.TraverseIn(tree.Root, func(n *Node) { fmt.Println(n.Value, ": ", n.Data, " | ") })
	fmt.Println()

	//single tree case
	fmt.Println("Single tree: ")
	tree = &Tree{}
	tree.Insert("a", "apache")
	tree.TraverseIn(tree.Root, func(n *Node) { fmt.Println(n.Value, ": ", n.Data, " | ") })
	fmt.Println()

	tree.Delete("a")
	fmt.Println("After delete:")
	tree.TraversePre(tree.Root, func(n *Node) { fmt.Print(n.Value, ": ", n.Data, " | ") })
	fmt.Println()
}
