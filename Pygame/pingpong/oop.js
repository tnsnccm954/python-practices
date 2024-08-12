let user = {
    // propert
    name: 'phuchiro',
    lastname: 'not weep for sure',

    //method | function
    introduce(){
        console.log('hello,', this.name)
        console.log('nice to meet ya')
    }
}
user.introduce()
// console.log('prev:',user)
// user.display_name = user.name + user.lastname
// console.log('current:',user)
console.log(user['name'])