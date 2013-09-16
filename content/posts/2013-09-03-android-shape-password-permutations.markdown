Title: Android Shape Password Generation
Author: Ross M. Donaldson
Date: 2013-09-13
Slug: 2013-09-13_android_shape_password_generation
Tags: Android, Problems, Scala
Category: Code
Summary: Taking a stab at generating the full set of legal Android shape passwords.
draft: True

My friend Steve recently posed an interesting challenge to me:

"i thought of it on the plane back from vermont, basically, calculating the potential passwords possible on an android phone."

Very interesting. The full problem statement goes a little like this:

* An Android Password has nine available nodes in a 3x3 grid.
* A valid password has no fewer than four and no more than nine nodes.
* A node can only connect to a "reachable" node -- that is, from the top left corner, your next move cannot be to the bottom right corner.

The rules of reach-ability are by far the trickiest bit of this. How do you tell a node which Other Node it can get to? Particularly without my personal pet problem: overflowing the heap. (Or the stack. Or both.)

Steve is one of the smartest computer scientists I know, has his Ph.D. , and deeply groks graph theory. I'm a musician-turned-hacker with too much free time and a dodgy understanding of the classic algorithms. His an my approaches? Likely to look very different. Here, I'll detail mine.

I started with the thought that the smallest conceptual unit here is a Node. Nodes build in to a Path. A Node should know its context, but a Path should know the rules of path-building -- including exceptions to the standard rules. Armed with this idea, I wrote two hundred-odd lines of Scala and melted the heap.

Fantastic.

As a programmer I operate in much the same way I do as a writer: when I'm writing serious essays, I write down *everything*, censoring as little as possible, just slathering the page in words. As I write more and more and more, I begin to perceive the underlying structure of what I'm up to -- and it's a structure I have to find a way to materialize outside my own head in order to understand it clearly. Then there's A Moment of Clarity, a click, when things suddenly drop in to place and I start removing chaff in huge chunks, carving away at the mass I created to leave an essential, spare Thing.

So with writing, so with my code. I wrote vastly more code than I needed, refactored, wrote more code, got it compiling, branched, and wrote more code until finally I noticed something incredibly simple:

One node can always reach any other node as long as you add the node that's "in the way" to the Path.

When I'm coding, I call this moment, "the Collapse". It's the point at which I can suddenly see the underlying structure I've been feeling out and I can work to realize it, when I can stop laying down material and start carving away at it. The above let me peel away more than half the code I'd put in place, and while the result wasn't bug free (editing still required), it was A) comprehensible, B) terse, C) fixable, and D) kinda elegant. It's this last that often is my surest indicator I'm on the right path -- when things stop looking less _eugh_ and more _oooh!_

The final product needs some space to run; I had planned it as an interactive demo on my web page, but it uses far more RAM than Heroku will allow me*. The code lives in its original state in my repo for gastove.com, but I also pulled it all together, like so:

```scala
import scala.math.abs

object AndroidPasswordGenerator{

  def main(args: Array[String]) {
    val grid = NodeGrid.generateGrid
    val paths = findPath(grid, new EmptyPath)
    paths.foreach{println}
  }

  def findPath(nodes: List[AndroidNode], path: AndroidPath): List[AndroidPath] = {
    nodes.flatMap{ node =>
       val newPath = path.addToPath(node)
       val remainingNodes = nodes.filter{ node =>
         !newPath.contains(node)
       }
       if (newPath.length >= 9) List(newPath)
       else if (newPath.length >= 4) findPath(remainingNodes, newPath) ++ List(newPath)
       else findPath(remainingNodes, newPath)
    }
  }
}

class AndroidNode(x: Int, y: Int) {

  lazy val neighbors = getAdjacentNodes

  override def toString(): String = "<" + this.x + "," + this.y + ">"

  def - (other: AndroidNode): AndroidNode = {
      new AndroidNode(diff(this.x, other.x), diff(this.y, other.y))
        }

  def diff(a: Int, b: Int): Int = {
      if (a == b) a else abs(a - b)
        }

  def getAdjacentNodes(): List[AndroidNode]= {
    def inRange(param: Int): Boolean = { (param > 0 && param < 4) }
    (-1 to 1)
      .toList
      .flatMap{ xMod =>
        (-1 to 1)
          .toList
          .map{ yMod =>
            AndroidNode(this.x + xMod, this.y + yMod)
          }
      }
    .filter{ node =>
      (inRange(node.x) && inRange(node.y)) && node != this
    }
  }

}

// Grid Generator
object NodeGrid {
  def generateGrid(): List[AndroidNode] = {
    (1 to 3).toList.flatMap{ x => (1 to 3).toList.map{y => AndroidNode(x, y)}}
  }
}

// Base Path Class
abstract class AndroidPath {
  val path: List[AndroidNode]
  def isEmpty(): Boolean
  def length(): Int
  def contains(node: AndroidNode): Boolean
  def addToPath(candidateNode: AndroidNode): AndroidPath
  def toString(): String
}

class EmptyPath extends AndroidPath {

  val path: List[AndroidNode] = List()
  def isEmpty() = true
  def length(): Int = 0
  def contains(node: AndroidNode): Boolean = false
  def addToPath(candidateNode: AndroidNode): AndroidPath =
    new Path(List(candidateNode))

  override def toString(): String = "<Empty Path>"

}

class Path(val path: List[AndroidNode]) extends AndroidPath {

  def length(): Int = this.path.length

  def isEmpty(): Boolean = false

  def contains(node: AndroidNode): Boolean = this.path.contains(node)

  def addToPath(candidateNode: AndroidNode): Path = {
    if (this.path.head.neighbors.contains(candidateNode))
      new Path(candidateNode +: this.path)
    else {
      val interstitial = getInterstitialNode(candidateNode)
      if (this.path.contains(interstitial))
        new Path(candidateNode +: this.path)
      else
        new Path(candidateNode +: interstitial +: this.path)
    }
  }

  def getInterstitialNode(candidateNode: AndroidNode): AndroidNode =
    this.path.head - candidateNode

  override def toString(): String =
      this.path.reverse.mkString("->")

}
```

Now, we just have to see how Steve solved it. Probably lasers.

[^1]: Which is not saying much. Heroku gives you 512mb per 1x Dyno. Feh.
n
