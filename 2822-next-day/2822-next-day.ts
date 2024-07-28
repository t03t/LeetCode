interface Date {
    nextDay(): string;
}

Date.prototype.nextDay = function(): string {
    const currentDate = new Date(this);
    currentDate.setDate(currentDate.getDate() + 1);
    console.log(currentDate);
    return `${currentDate.getFullYear()}-${(currentDate.getMonth()+1).toString().padStart(2, '0')}-${currentDate.getDate().toString().padStart(2, '0')}`;
}

/**
 * const date = new Date("2014-06-20");
 * date.nextDay(); // "2014-06-21"
 */