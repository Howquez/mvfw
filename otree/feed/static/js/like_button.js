console.log("like button ready!");

var attention_check = document.getElementById("attention_check");
attention_check.addEventListener("click", function() {
    var hidden_field = document.getElementById("liked_item_attention");
    hidden_field.value = 'True'
    }
)
