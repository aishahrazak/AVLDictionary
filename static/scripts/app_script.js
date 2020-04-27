
$(function () {
    $('#addBtn').bind('click', function () {
        var word = $('#word').val();
        if (word == null || word == undefined || word.length == 0) {
            alert("Word cannot be empty.");
        }
        var meaning = $('#meaning').val();
        if (meaning == null || meaning == undefined || meaning.length == 0) {
            alert("Meaning cannot be empty");
        }
        $.getJSON("/addWord", { word: word, meaning: meaning },
            function (data) {
                //showValues(data);
                printTree(data);
            });
    });

    $('#searchBtn').bind('click', function (){
        var word = $('#word').val();
        if (word == null || word == undefined || word.length == 0) {
            alert("Word cannot be empty.");
        }
        $("#meaning").css('background', 'grey');
        $.getJSON("/searchWord", { word: word },
            function (data) {
                console.log(data);
                $("#meaning").val(data);
            });
    });

    $('#deleteBtn').bind('click', function () {
        var word = $('#word').val();
        if (word == null || word == undefined || word.length == 0) {
            alert("Word cannot be empty.");
        }
        $.getJSON("/deleteWord", { word: word },
            function (data) {
                printTree(data);
            });
    });

    $('#resetBtn').bind('click', function () {
        $("p#tree").empty();
        $.getJSON("/reset", function (data) { console.log(data); });
    });

    $('#listBtn').bind('click', function(){
        $.getJSON("/getList", 
            function(data){
                showValues(data);
            })
    });

    function showValues(data){
        $("p#tree").empty();
        var nodes = data;
        console.log("No of words:" + nodes.length);
        for (n of nodes) {
            console.log("key:" + n.key + " bf:" + n.balanceFactor);
            $("#tree").append(`<span class="node">${n.key}(value = ${n.value})</span><br/><br/>`);
        }
    };

    function printTree(data) {
        $("p#tree").empty();
        var nodes = data;
        var n = nodes.length;
        //no of levels in the tree
        var height = Math.ceil(Math.log2((n+1)/2));
        var curLevel = 0;
        var maxNoOfNodesAtLevel = Math.pow(2,curLevel);
        var j = 0;
        while(curLevel <= height){
            for(k=0; k<maxNoOfNodesAtLevel; k++){
                if(nodes[j] != null){
                    $("#tree").append(`<span class="node">${nodes[j].key}(bf = ${nodes[j].balanceFactor})</span>\n`);   
                    j++;
                }
            }
            $("#tree").append(`<br/><br/>`);
            curLevel++;
            maxNoOfNodesAtLevel = Math.pow(2,curLevel);
        }       
    };
});
