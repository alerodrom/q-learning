from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView

from qlearning.qlearning import Qlearning

class CreateMapView(TemplateView):
    
    def create_map(request):
        return render(request, "app/create_map.html")

class HomePageView(TemplateView):
    template_name = "app/home.html"

    def get_context_data(self, **kwargs):
        ql = Qlearning(init_zeros=False, print_steps=False)
        result = ql.call()

        context = super(HomePageView, self).get_context_data(**kwargs)
        context["maps"] = result["maps"]
        context["result"] = result["result"]
        # context["maps"] = [
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>2</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>2</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>2</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>2</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>2</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>2</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>2</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>4</td>\n      <td>2</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>4</td>\n      <td>2</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>X</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        #     '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n      <th>9</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>0</td>\n      <td>0</td>\n      <td>X</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>X</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1</td>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n      <td>X</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>4</td>\n      <td>4</td>\n      <td>4</td>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1</td>\n      <td>X</td>\n      <td>X</td>\n      <td>2</td>\n      <td>2</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1</td>\n      <td>X</td>\n      <td>1</td>\n      <td>1</td>\n      <td>2</td>\n      <td>2</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n    </tr>\n  </tbody>\n</table>',
        # ]
        # context["result"] = {
        #     "steps": 16,
        #     "reward": 625,
        #     "path": [
        #         [(5, 1), 1],
        #         [(4, 1), 2],
        #         [(4, 2), 1],
        #         [(4, 1), 0],
        #         [(3, 1), 2],
        #         [(3, 2), 1],
        #         [(2, 2), 2],
        #         [(2, 3), 1],
        #         [(2, 4), 1],
        #         [(2, 5), 1],
        #         [(2, 6), 1],
        #         [(2, 7), 1],
        #         [(2, 8), 1],
        #         [(2, 9), 1],
        #         [(1, 9), 2],
        #         [(0, 9), 2],
        #     ],
        # } 
        return context
