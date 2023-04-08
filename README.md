# GenderGame
Program can guess the gender of given the given name based on the country id.

![gender](https://user-images.githubusercontent.com/29086241/228649894-ba8f7628-5d17-4a1b-879e-d0694910068f.png)

<h2>Country names and their id</h2>
IN  	India <br>
GB	United Kingdom <br> <br>
It is recommended to check the count of the response when using localization. If the count is very low or gender is null, you can fallback to a request with no localization.
<p class="MuiTypography-root MuiTypography-body1 MuiTypography-paragraph" style="font-weight: 300;">All services follow <a class="MuiTypography-root MuiLink-root MuiLink-underlineHover MuiTypography-colorPrimary" href="http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" style="color: rgb(0, 136, 204);">ISO 3166-1 alpha-2</a> for country codes. Check <a class="MuiTypography-root MuiLink-root MuiLink-underlineHover MuiTypography-colorPrimary" href="/our-data" style="color: rgb(0, 136, 204);">our data</a> to see a list of all supported countries.</p>

<h2>USE CASES</h2>
<h3>What other people are using gender prediction for:- </h3>
People use gender classification for a lot things. Here you'll find a selected list of articles and projects that use Genderize.io, Agify.io or Nationalize.io to determine the gender, age and nationality of names.

<h2 class="MuiTypography-root jss3 MuiTypography-h2" style="font-size: 1.75rem; font-weight: 300;">How we analysed 70 million comments on the Guardian website</h2>
<p class="MuiTypography-root jss4 MuiTypography-body1" style="font-weight: 300;">In this report, The Guardian analyses 70 million comments posted on their website. It provides quantitative evidence for online abuse and trolling. The result in short: Out of the 10 most abused writers, 8 were women. The two men were black.</p>
<a class="MuiTypography-root MuiLink-root MuiLink-underlineHover MuiTypography-colorPrimary" href="https://www.theguardian.com/technology/2016/apr/12/how-we-analysed-70m-comments-guardian-website" target="_BLANK" style="color: rgb(0, 136, 204);">Read article</a>


<h6 class="MuiTypography-root jss5 MuiTypography-subtitle2">The Atlantic<span class="MuiTypography-root MuiTypography-caption">&nbsp;by Ed Yong</span></h6>
<h2 class="MuiTypography-root jss3 MuiTypography-h2" style="font-size: 1.75rem; font-weight: 300;">When Will the Gender Gap in Science Disappear?</h2>
<a class="MuiTypography-root MuiLink-root MuiLink-underlineHover MuiTypography-colorPrimary" href="https://www.theatlantic.com/science/archive/2018/04/when-will-the-gender-gap-in-science-disappear/558413/" target="_BLANK" style="color: rgb(0, 136, 204);">Read article</a>



<h6 class="MuiTypography-root jss5 MuiTypography-subtitle2">The Washington Post<span class="MuiTypography-root MuiTypography-caption">&nbsp;by Philip Bump</span></h6>
<h2 class="MuiTypography-root jss3 MuiTypography-h2" style="font-size: 1.75rem; font-weight: 300;">Here’s how Hillary Clinton knows that 61 percent of her donors were women</h2>
<a class="MuiTypography-root MuiLink-root MuiLink-underlineHover MuiTypography-colorPrimary" href="https://www.washingtonpost.com/news/the-fix/wp/2015/07/16/heres-how-hillary-clinton-knows-that-61-percent-of-her-donors-were-women" target="_BLANK" style="color: rgb(0, 136, 204);">Read article</a>





python 3.x
pip install requests

#requests 2.28.2
This library will be used for making requests to the API
Requests allows you to send HTTP/1.1 requests extremely easily. 
There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!
Requests is one of the most downloaded Python packages today, pulling in around 30M downloads / week— according to GitHub, Requests is currently depended upon by 1,000,000+ repositories. You may certainly put your trust in this code.







#The url that we will be using will take this format:
https://api.genderize.io?name={YOUR_NAME}

#The genderize.io website provides a playground where you can test the API.
#The API is free for up to 1000 names/day.

The request will render a response like the following:

{
  "name": "YOUR_NAME",
  "gender": "male",
  "probability": 0.99,
  "count": 165452
}

The probability indicates the certainty of the assigned gender. 
Basically the ratio of male to females. 
The count represents the number of data rows examined in order to calculate the response.

#Batch usage
Checking the gender of multiple names in a request
You can infer the gender of up to 10 names at a time. To do so, send an array of names as the "name" parameter.

https://api.genderize.io/?name[]=peter&name[]=lois&name[]=stevie



#Localization
Classifying genders in the scope of a specific country
Naming conventions can rely heavily on demographics. Therefore, the API accepts an optional "country_id" parameter, for when you have that information. 
In a lot of cases, this will make the guess more correct.

https://api.genderize.io?name=peter&country_id=US






#Responses & Errors
How to understand your gender checking
All responses wil be in "content-type: application/json; charset=utf-8".

Here's a list of the errors the API can respond with. Some of them will only apply if you're using an API key.

401 - Unautherized

{ "error": "Invalid API key" }
402 - Payment Required

{ "error": "Subscription is not active" }
422 - Unprocessable Entity

{ "error": "Missing 'name' parameter" }
422 - Unprocessable Entity

{ "error": "Invalid 'name' parameter" }
429 - Too Many Requests

{ "error": "Request limit reached" }
429 - Too Many Requests

{ "error": "Request limit too low to process request" }


