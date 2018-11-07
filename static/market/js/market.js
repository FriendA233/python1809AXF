$(function () {
    $('.market').width(innerWidth)

//    获取typeIndex
    typeIndex = $.cookie('typeIndex')
    if (typeIndex) {  //已经有点击分类
        $('.type-slider .type-item').eq(typeIndex).addClass('active')
    } else {  //没有点击分类
        //没有点击分类默认第一个
        $('.type-slider .type-item:first').addClass('active')

    }

//    侧边栏
//    问题：点击时，样式已经添加，但这是a标签，点击后需要重新获取页面，即重新刷新页面。
//      样式就会恢复到原来的。
//    解决：点击时，记录点击的位置。
//    当页面刷新后，js就获取记录的位置，并设置对应的样式。
//    cookie
//    设置cookie
//     $.(key,value,options)   options >> {expires:过期时间,path:路径}
    //    获取cookie
//    $.(key)
//    删除cookie
//    $.(key,null)
    $('.type-item').click(function () {
        // $(this).addClass('active')
        //    记录位置
        $.cookie('typeIndex', $(this).index(), {expires: 3, path: '/'})
    })

//    分类按钮
    categoryBt = false
    $('#categoryBt').click(function () {
        //    取反
        categoryBt = !categoryBt

        categoryBt ? categoryviewShow() : categoryviewHide()

    })

//    排序按钮
    sortBt = false
    $('#sortBt').click(function () {
        //取反
        sortBt = !sortBt
        sortBt ? sortviewShow() : sortviewHide()
    })

    //    灰色蒙层
    $('.bounce-view').click(function () {
        categoryBt = false
        sortBt = false
        categoryviewHide()
        sortviewHide()
    })

    function categoryviewShow() {
        sortBt = false
        sortviewHide()
        $('.bounce-view.category-view').show()
        $('#categoryBt i').removeClass('glyphicon glyphicon-triangle-top').addClass('glyphicon glyphicon-triangle-bottom')
    }

    function categoryviewHide() {
        $('.bounce-view.category-view').hide()
        $('#categoryBt i').removeClass('glyphicon glyphicon-triangle-bottom').addClass('glyphicon glyphicon-triangle-top')
    }

    function sortviewShow() {
        categoryBt = false
        categoryviewHide()
        $('.bounce-view.sort-view').show()
        $('#sortBt i').removeClass('glyphicon glyphicon-triangle-top').addClass('glyphicon glyphicon-triangle-bottom')
    }

    function sortviewHide() {
        $('.bounce-view.sort-view').hide()
        $('#sortBt i').removeClass('glyphicon glyphicon-triangle-bottom').addClass('glyphicon glyphicon-triangle-top')
    }


//    购物车操作
    $('.bt-wrapper .glyphicon-minus').hide()
    $('.bt-wrapper .num').hide()

//    有商品数据的,即要显示,否则不显示
    $('.bt-wrapper .num').each(function () {
        var num = parseInt($(this).html())
        if (num){
            $(this).show()
            $(this).prev().show()
        }
    })

//   加操作
    $('.bt-wrapper .glyphicon-plus').click(function () {
        //商品ID
        var goodsid = $(this).attr('goodsid')
        //that为了解决ajax中this的问题
        var $that = $(this)
        $.get('/addcart/', {'goodsid': goodsid}, function (response) {
            console.log(response)
            if (response.status == -1) {
                window.open('/login/', target = '_self')
            }
            else if (response.status == 1) {
                //错误的!!!!
                // $('.bt-wrapper .glyphicon-minus').show()
                // $('.bt-wrapper .num').show().html(response.number)
                //    只修改当前的
                // $(this).prev().show().html(response.number)
                // $(this).prev().prev().show()
                $that.prev().show().html(response.number)
                $that.prev().prev().show()
            }
        })
    })
//    减操作
    $('.bt-wrapper .glyphicon-minus').click(function () {
        var goodsid = $(this).attr('goodsid')
        var $that = $(this)
    //    发起ajax请求
        $.get('/subcart/',{'goodsid':goodsid},function (response) {
            console.log(response)
            if(response.status==1){
                var number = response.number
                if(number > 0){  //显示
                    $that.next().html(number)
                }else {  //隐藏
                    $that.next().hide()
                    $that.hide()
                }
            }
        })
    })
})