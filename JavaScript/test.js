// const obj = {
//   a: 1,

//   this1: function() {
//     console.log(this.a)
//   },

//   this2: () => {
//     console.log(this.a)
//   }
// }

// obj.test1() // 1
// obj.test2() // undefined

myFunc = function() {
  console.log(this.a)
}

const a = 1
const obj ={
  a: 2,
  print: function(func){
    func()
  }
}

obj.print(myFunc)