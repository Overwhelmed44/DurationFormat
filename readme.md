<h1 align="center">
    Duration Format (Russian)
</h1>
<h3>
    Class which formats a duration, given as a number of seconds, in a human-friendly way.
    The class accepts a non-negative integer.
    The duration is expressed as a combination of years, weeks, days, hours, minutes and seconds
    separated by a comma and a space.<br><br>
    Examples:
</h3>
<ul>
    <li>print(DurationFormat(18365191)) --> 30&nbspнедель, 2&nbspдня, 13&nbspчасов, 26&nbspминут и 31&nbspсекунда</li>
    <li>print(DurationFormat(19756183571)) --> 626&nbspлет, 24&nbspнедели, 1&nbspдень, 12&nbspчасов, 46&nbspминут и 11&nbspсекунд</li>
    <li>print(DurationFormat(3601)) --> 1&nbspчас и 1&nbspсекунда</li>
</ul>
