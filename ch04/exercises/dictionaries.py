article = "A Problem in Need of a Creative Solution In the 1870s, newspapers and printers faced a very specific and very costly problem. Photography was a new and exciting medium at the time. Readers wanted to see more pictures, but nobody could figure out how to print images quickly and cheaply.For example, if a newspaper wanted to print an image in the 1870s, they had to commission an engraver to etch a copy of the photograph onto a steel plate by hand. These plates were used to press the image onto the page, but they often broke after just a few uses. This process of photoengraving, you can imagine, was remarkably time consuming and expensive.The man who invented a solution to this problem was named Frederic Eugene Ives. He went on to become a trailblazer in the field of photography and held over 70 patents by the end of his career. His story of creativity and innovation, which I will share now, is a useful case study for understanding the 5 key steps of the creative process."

substitutions = {
  "Commission":"Money",
  "print": "copy of article",
  "creative":"crazy",
   "study":"fifth harmony"}

for key, value in substitutions.items(): 
 article = article.replace(key,value)

print(article)