# Covid Data Exercise
Data Science Exercise with data from [Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)

## System Requirements
Require  Python3.6+

```shell
$ pip install pyecharts requests pandas numpy datetime wget -U

```
### For MacOS
Use Homebrew to install wget
```shell
brew install wget
```
### html preview

US Covid Map:

[Confirmed cases](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/UScovid_confirmed.html)
[Death cases](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/UScovid_death.html)
[Combine](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/UScovid_combine.html)



Each State Trend:

[Alabama](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Alabama.html)
[Alaska](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Alaska.html)
[Arizona](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Arizona.html)
[Arkansas](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Arkansas.html)
[California](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/California.html)
[Colorado](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Colorado.html)
[Connecticut](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Connecticut.html)
[Delaware](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Delaware.html)
[District of Columbia](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/District%20of%20Columbia.html)
[Florida](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Florida.html)
[Georgia](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Georgia.html)
[Hawaii](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Hawaii.html)
[Idaho](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Idaho.html)
[Illinois](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Illinois.html)
[Indiana](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Indiana.html)
[Iowa](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Iowa.html)
[Kansas](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Kansas.html)
[Kentucky](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Kentucky.html)
[Louisiana](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Louisiana.html)
[Maine](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Maine.html)
[Maryland](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Maryland.html)
[Massachusetts](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Massachusetts.html)
[Michigan](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Michigan.html)
[Minnesota](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Minnesota.html)
[Mississippi](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Mississippi.html)
[Missouri](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Missouri.html)
[Montana](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Montana.html)
[Nebraska](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Nebraska.html)
[Nevada](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Nevada.html)
[New Hampshire](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/New%20Hampshire.html)
[New Jersey](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/New%20Jersey.html)
[New Mexico](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/New%20Mexico.html)
[New York](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/New%20York.html)
[North Carolina](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/North%20Carolina.html)
[North Dakota](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/North%20Dakota.html)
[Ohio](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Ohio.html)
[Oklahoma](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Oklahoma.html)
[Oregon](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Oregon.html)
[Pennsylvania](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Pennsylvania.html)
[Puerto Rico](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Puerto%20Rico.html)
[Rhode Island](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Rhode%20Island.html)
[South Carolina](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/South%20Carolina.html)
[South Dakota](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/South%20Dakota.html)
[Tennessee](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Tennessee.html)
[Texas](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Texas.html)
[Utah](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Utah.html)
[Vermont](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Vermont.html)
[Virginia](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Virginia.html)
[Washington](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Washington.html)
[West Virginia](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/West%20Virginia.html)
[Wisconsin](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Wisconsin.html)
[Wyoming](https://htmlpreview.github.io/?https://github.com/JiaZhou-PU/JiaZhou-PU.github.io/blob/main/eachstate/Wyoming.html)


