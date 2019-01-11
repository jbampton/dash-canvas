# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashCanvas(Component):
    """A DashCanvas component.
Canvas component for drawing on a background image and selecting
regions.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- label (string; optional): A label that will be printed when this component is rendered.
- image_content (string; optional): Image data string, formatted as png or jpg data string. Can be
generated by utils.io_utils.array_to_data_string.
- zoom (number; optional): Zoom factor
- width (number; optional): Width of the canvas
- height (number; optional): Height of the canvas
- scale (number; optional): Scaling ratio between canvas width and image width
- tool (string; optional): Selection of drawing tool, among ["pencil", "pan", "circle",
"select"].
- lineWidth (number; optional): Width of drawing line (in pencil mode)
- lineColor (string; optional): Color of drawing line (in pencil mode). Can be a text string,
like 'yellow', 'red', or a color triplet like 'rgb(255, 0, 0)'.
Alpha is possible with 'rgba(255, 0, 0, 0.5)'.
- filename (string; optional): Name of image file to load (URL string)
- tmp (number; optional): Counter of how many times the save button was pressed
(to be used mostly as input)
- trigger (number; optional): Counter of how many times the save button was pressed
(to be used mostly as input)
- json_data (string; optional): Sketch content as JSON string, containing background image and
annotations. Use utils.parse_json.parse_jsonstring to parse
this string.

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, label=Component.UNDEFINED, image_content=Component.UNDEFINED, zoom=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, scale=Component.UNDEFINED, tool=Component.UNDEFINED, lineWidth=Component.UNDEFINED, lineColor=Component.UNDEFINED, filename=Component.UNDEFINED, tmp=Component.UNDEFINED, trigger=Component.UNDEFINED, json_data=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'label', 'image_content', 'zoom', 'width', 'height', 'scale', 'tool', 'lineWidth', 'lineColor', 'filename', 'tmp', 'trigger', 'json_data']
        self._type = 'DashCanvas'
        self._namespace = 'dash_canvas'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'label', 'image_content', 'zoom', 'width', 'height', 'scale', 'tool', 'lineWidth', 'lineColor', 'filename', 'tmp', 'trigger', 'json_data']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashCanvas, self).__init__(**args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('DashCanvas(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'DashCanvas(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
