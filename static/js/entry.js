/*
entry.js

2019/2/7 y.ikeda
*/

$(document).ready(function(){
    test1();
    
    $("#btn_regist_stayorder").click(function(){
        regist();
    });
    $("#btn_regist_reorder").click(function(){
        // ランダムで順序を入れ替える
        var cur_members = $("#area_players").val().split(/[\r\n]+/);
        for(var i = cur_members.length - 1; i > 0; i--){
            var r = Math.floor(Math.random() * (i + 1));
            var tmp = cur_members[i];
            cur_members[i] = cur_members[r];
            cur_members[r] = tmp;
        }
        // 空白があったら削除
        for(var i=cur_members.length-1; i>0; i--){
            if( cur_members[i] == "" ){
                cur_members.splice(i, 1);
            }
        }
        $("#area_players").val(cur_members.join("\n"));

        regist();
    });
});


function regist(){
    //var cur_members = $("#area_players").val().split(/[\r\n]+/);
    
    // post
    $("#frmRegist").submit();
}

function test1(){
    function set_placeholder_val(id){
        var v = $(id).attr("placeholder");
        $(id).val(v);
    }
    set_placeholder_val("#txt_tournament_name");
    set_placeholder_val("#area_detail");
    set_placeholder_val("#area_players");
    
}
