function calculate() {
    var num1 = document.getElementById("num1").value;
    var num2 = document.getElementById("num2").value;
    var value1 = document.getElementById("value1").value;
    var value2 = document.getElementById("value2").value;
    var operation = document.getElementById("operation").value;

    eel.calc(num1,num2,value1,value2,operation)

    }
    function output(denary, binary, hexa) {
        console.log(denary)
        console.log(binary)
        var output_den = document.getElementById("denary");
        output_den.innerHTML += "<br>" + denary;
        var output_bin = document.getElementById("binary");
        output_bin.innerHTML += "<br>" + binary;
        var output_hexa = document.getElementById("hexa");
        output_hexa.innerHTML += "<br>" + hexa;
    }
    eel.expose(output);