$(function () {
    $('.login').width(innerWidth)
})

//账号验证
$('#account input').blur(function () {
    if ($(this).val()=='') return
    //字母数字
    var reg = /^[A-Za-z0-9]+$/
    if (reg.test($(this).val())){
        $('#account i').html('')
        $('#account').removeClass('has-error').addClass('has-success')
        $('#account span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
    } else {  //不符合
        $('#account i').html('账号由字母，数字组成')
        $('#account').removeClass('has-success').addClass('has-error')
        $('#account span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
    }
})

//密码验证
$('#password input').blur(function () {
    if ($(this).val()=='') return
    //数字
    var reg = /^[\d]{6,12}$/
    if (reg.test($(this).val())){
        $('#password i').html('')
        $('#password').removeClass('has-error').addClass('has-success')
        $('#password span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
    } else {
        $('#password i').html('6~12位数字')
        $('#password').removeClass('has-success').addClass('has-error')
        $('#password span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
    }
})