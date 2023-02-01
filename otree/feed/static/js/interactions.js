console.log("interactions button ready!");

// var likeButton = document.querySelector(".like-button");
// var likeCount = document.querySelector(".like-count");
// var likeIcon = document.querySelector(".like-icon");

// likeButton.addEventListener("click", function() {
//     if (likeButton.classList.contains("liked")) {
//         likeButton.classList.remove("liked");
//         likeCount.textContent = (parseInt(likeCount.textContent) - 1).toString();
//         likeIcon.className="bi bi-heart text-secondary like-icon";

//     } else {
//         likeButton.classList.add("liked");
//         likeCount.textContent = (parseInt(likeCount.textContent) + 1).toString();
//         likeIcon.className="bi bi-heart-fill text-danger like-icon";
//     }
// });


var replyButtons = document.querySelectorAll(".reply-button");

replyButtons.forEach(function(replyButton) {
    var replyCount = replyButton.querySelector(".reply-count");
    var replyIcon  = replyButton.querySelector(".reply-icon");

    replyButton.addEventListener("click", function() {
      if (replyButton.classList.contains("replied")) {
        replyButton.classList.remove("replied");
        replyCount.textContent = (parseInt(replyCount.textContent) - 1).toString();
        replyIcon.className="bi bi-chat text-secondary reply-icon";
    } else {
        replyButton.classList.add("replied");
        replyCount.textContent = (parseInt(replyCount.textContent) + 1).toString();
        replyIcon.className="bi bi-chat-fill text-primary reply-icon";
    }
});
});


var retweetButtons = document.querySelectorAll(".retweet-button");

retweetButtons.forEach(function(retweetButton) {
    var retweetCount = retweetButton.querySelector(".retweet-count");
    var retweetIcon  = retweetButton.querySelector(".retweet-icon");

    retweetButton.addEventListener("click", function() {
      if (retweetButton.classList.contains("retweeted")) {
        retweetButton.classList.remove("retweeted");
        retweetCount.textContent = (parseInt(retweetCount.textContent) - 1).toString();
        retweetIcon.className="bi bi-arrow-repeat text-secondary retweet-icon";
        retweetIcon.removeAttribute("style")
    } else {
        retweetButton.classList.add("retweeted");
        retweetCount.textContent = (parseInt(retweetCount.textContent) + 1).toString();
        retweetIcon.className="bi bi-arrow-repeat text-primary retweet-icon";
        retweetIcon.style="-webkit-text-stroke: 0.5px"
    }
});
});


var likeButtons = document.querySelectorAll(".like-button");

likeButtons.forEach(function(likeButton) {
    var likeCount = likeButton.querySelector(".like-count");
    var likeIcon  = likeButton.querySelector(".like-icon");

    likeButton.addEventListener("click", function() {
      if (likeButton.classList.contains("liked")) {
        likeButton.classList.remove("liked");
        likeCount.textContent = (parseInt(likeCount.textContent) - 1).toString();
        likeIcon.className="bi bi-heart text-secondary like-icon";
    } else {
        likeButton.classList.add("liked");
        likeCount.textContent = (parseInt(likeCount.textContent) + 1).toString();
        likeIcon.className="bi bi-heart-fill text-danger like-icon";
    }
});
});


var shareButtons = document.querySelectorAll(".share-button");

shareButtons.forEach(function(shareButton) {
    var shareIcon  = shareButton.querySelector(".share-icon");

    shareButton.addEventListener("click", function() {
      if (shareButton.classList.contains("shared")) {
        shareButton.classList.remove("shared");
        shareIcon.className="bi bi-upload text-secondary share-icon";
        shareIcon.removeAttribute("style")
    } else {
        shareButton.classList.add("shared");
        shareIcon.className="bi bi-upload text-primary share-icon";
        shareIcon.style="-webkit-text-stroke: 0.5px"
    }
});
});