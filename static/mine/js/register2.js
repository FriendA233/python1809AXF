$(function () {
    $('.register').width(innerWidth)
})

//账号验证
$('#account input').blur(function () {
    if ($(this).val()=='') return
    //字母数字
    var reg = /^[A-Za-z0-9]+$/
    if (reg.test($(this).val())){
    //    ajax,获取账号是否可用
        $.get('/checkaccount/',{'account':$(this).val()},function (response) {
            console.log(response)
            console.log(response.status)
            if(response.status == 1){  //可用
                $('#account i').html('')
                $('#account').removeClass('has-error').addClass('has-success')
                $('#account span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
            }
            else{  //不可用
                $('#account i').html(response.msg)
                $('#account').removeClass('has-success').addClass('has-error')
                $('#account span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
            }
        })
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


//确认密码
$('#passwd input').blur(function () {
     if ($(this).val()=='') return
    if ($(this).val()==$('#password input').val()) {
        $('#passwd i').html('')
        $('#passwd').removeClass('has-error').addClass('has-success')
        $('#passwd span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
    } else {
        $('#passwd i').html('两次密码不一致')
        $('#passwd').removeClass('has-success').addClass('has-error')
        $('#passwd span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
    }
})



//名字验证
$('#name input').blur(function () {
    if ($(this).val()=='') return

    $('#name').removeClass('has-error').addClass('has-success')
    $('#name span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
})

//手机验证
$('#phone input').blur(function () {
     if ($(this).val()=='') return
    //数字
    var reg = /^1[3|5|7|8]\d{9}$/
    if (reg.test($(this).val())){
        $('#phone i').html('')
        $('#phone').removeClass('has-error').addClass('has-success')
        $('#phone span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
    } else {
        $('#phone i').html('请输入正确的手机号')
        $('#phone').removeClass('has-success').addClass('has-error')
        $('#phone span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
    }
})


//地址验证
$('#addr input').blur(function () {
    if ($(this).val()=='') return

    $('#addr').removeClass('has-error').addClass('has-success')
    $('#addr span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
})

