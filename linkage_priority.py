import arcpy
class ToolValidator(object):
  """Class for validating a tool's parameter values and controlling
  the behavior of the tool's dialog."""

  def __init__(self):
    """Setup arcpy and the list of tool parameters."""
    self.params = arcpy.GetParameterInfo()
    self.core_params = [12, 13, 14]
    self.climate_params = range(17, 27)
    self.wt_params = [28, 29, 30, 31]

  def initializeParameters(self):
    """Refine the properties of a tool's parameters.  This method is
    called when the tool is opened."""
    return

  def updateParameters(self):
    """Modify the values and properties of parameters before internal
    validation is performed.  This method is called whenever a parameter
    has been changed."""
    if self.params[11].value:
        for i in self.core_params:
            self.params[i].enabled = True
    else:
        for i in self.core_params:
            self.params[i].value = None
            self.params[i].enabled = False
    
    if self.params[14].value:
	self.params[30].enabled = True
    else:
        self.params[30].enabled = False

    if self.params[15].value:
        self.params[16].enabled = True
        self.params[31].enabled = True
        #if self.wt_unaltered:
        #   self.params[27].value = 0.25
        #   self.params[28].value = 0.25
        #   self.params[29].value = 0.25
        #   self.params[31].value = 0.25
    else:
        self.params[16].value = False
        self.params[16].enabled = False
        self.params[31].enabled = False

    if self.params[16].value:
        for i in self.climate_params:
            self.params[i].enabled = True
    else:
        for i in self.climate_params:
            self.params[i].enabled = False
    return

  def updateMessages(self):
    """Modify the messages created by internal validation for each tool
    parameter.  This method is called after internal validation."""
    if self.params[11].value is None:
        for i in self.core_params:
            self.params[i].clearMessage()
    return

  def wt_unaltered():
    """Check if weights have been altered."""
    unaltered = True
    for param in self.wt_params:
        if param.altered:
	    unaltered = False
	    break
    return unaltered
