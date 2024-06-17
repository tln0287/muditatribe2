// Sidebar - menu click and dropdown selection
$(".sidebar .nav-links   li:has(ul.sub-menu:not(.blank))").on("click", function () {
    var ele = this;
    $(".sidebar .nav-links   li:has(ul.sub-menu:not(.blank))").each(function (index) {
        if (ele != this)
            $(this).removeClass("showMenu");
        if (index == $(".sidebar .nav-links   li:has(ul.sub-menu:not(.blank))").length - 1) $(ele).toggleClass("showMenu");
    });

});

$(".sub-menu:has(a.sub-menu-link:not(.blank))").on("click", function () {
    var ele = this;
    $(".sub-menu:has(a.sub-menu-link:not(.blank))").each(function (index) {
        if (ele != this)
            $(this).removeClass("active");
        if (index == $(".sub-menu :has(a.sub-menu-link:not(.blank))").length - 1) $(ele).toggleClass("active");
    });

});


let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector("#menuToggle");
let sidebarBg = document.querySelector(".sidebar-bg");
sidebarBtn.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    sidebarBg.classList.toggle("close");
});

sidebarBg.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    sidebarBg.classList.toggle("close");
})


const profile_pic = document.getElementById('profile_pic');
const subMenu = document.getElementById('subMenu');
profile_pic.onclick = function () {
    quickmenu.classList.remove('open-menu');
    subMenu.classList.toggle('open-menu');
}

const menu = document.getElementById('menu');
const quickmenu = document.getElementById('quickmenu');
menu.onclick = function () {
    subMenu.classList.remove('open-menu');
    quickmenu.classList.toggle('open-menu');
}

const homesection = document.getElementById('homeSection');
homesection.onclick = function () {
    subMenu.classList.remove('open-menu');
    quickmenu.classList.remove('open-menu');
}



// Textarea auto height

$("textarea").each(function (index, element) {

    this.style.height = this.scrollHeight + "px";

    this.style.overflow = "hidden";

}).on("input", function () {

    this.style.height = this.scrollHeight + "px";
});

jQuery(function ($) {
    $(" .sidebar ul li a")
        .click(function (e) {
            var link = $(this);

            var item = link.parent("li a");

            if (item.hasClass("active")) {
                item.removeClass("active").children("a").removeClass("active");
            } else {
                item.addClass("active").children("a").addClass("active");
            }

            if (item.children("ul").length > 0) {
                var href = link.attr("href");
                link.attr("href", "#");
                setTimeout(function () {
                    link.attr("href", href);
                }, 300);
                e.preventDefault();
            }
        })
        .each(function () {
            var link = $(this);
            if (link.get(0).href === location.href) {
                link.addClass("active").parents("li").addClass("active");
                return false;
            }
        });
});


function generateUUID() {
    var d = new Date().getTime();
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = (d + Math.random() * 16) % 16 | 0;
        d = Math.floor(d / 16);
        return (c == 'x' ? r : (r & 0x7 | 0x8)).toString(16);
    });
    return uuid;
};