(function() {
    var dayInput = document.getElementById('day-input');
    var leftImg = document.getElementById('left-img');
    var rightImg = document.getElementById('right-img');

    var updateImgUrl = function() {
        var day = dayInput.value;
        updateImgUrlInner(day, leftImg, leftMapping);
        updateImgUrlInner(day, rightImg, rightMapping);
    };

    var updateImgUrlInner = function(day, img, mapping) {
        img.setAttribute('src', '');
        if (mapping.hasOwnProperty(day)) {
            img.setAttribute('src', mapping[day]);
        } else {
            img.setAttribute('src', sorryUrl);
        }
    };

    var setLimitOnDayInput = function() {
        var leftDays = Object.keys(leftMapping);
        var rightDays = Object.keys(rightMapping);
        var allDays = leftDays.concat(rightDays).map(function(day) { return parseInt(day); });
        var maxDay = allDays.reduce(function(day1, day2) { return Math.max(day1, day2); })
        var minDay = allDays.reduce(function(day1, day2) { return Math.min(day1, day2); })
        dayInput.setAttribute('max', maxDay);
        dayInput.setAttribute('min', minDay);
    };

    dayInput.addEventListener('change', updateImgUrl);
    dayInput.focus();

    updateImgUrl();
    setLimitOnDayInput();
})();
