$( document ).ready(function() {
    $('.link-icon').on('click', function (e) {
        window.open($(this).data('recipelink'));
    });

    const $recipeGrid = $('#recipe-flex-container');
    const baseWidth = $recipeGrid.children().eq(0).width();


    $('.recipe-item').on('click', function(e) {
        let recipeDetails = $('#recipe-'+ $(this).data('recipepk'));
        let currentHeight = $recipeGrid.height();

        let newHeight = currentHeight + recipeDetails.get(0).scrollHeight;
        if ($(this).hasClass('expanded')) {
            newHeight = currentHeight - recipeDetails.get(0).scrollHeight;
        }
        $recipeGrid.height(newHeight.toString() + 'px');

        $(this).toggleClass('expanded');
    });

    function setFlexHeight() {
        let cols = Math.floor(window.innerWidth / baseWidth);
        let itemsInCol = Math.ceil($recipeGrid.children().length / cols);
        let maxItemHeight = 250;
        for (let i = 0; i < $recipeGrid.children().length; i++) {
            const currentHeight = $recipeGrid.children().eq(i).height();
            if (currentHeight > maxItemHeight) {
                maxItemHeight = currentHeight;
            }
        }
        $recipeGrid.height(itemsInCol * maxItemHeight);
    }

    window.onload = function () {
      setFlexHeight();
    };

    window.onresize = function () {
      setFlexHeight();
    };
});
