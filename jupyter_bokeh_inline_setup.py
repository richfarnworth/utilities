#Allows Bokeh charts to be displayed inline in a Jupyter notebook

from bokeh.resources import INLINE
import bokeh.io

bokeh.io.output_notebook(INLINE)
