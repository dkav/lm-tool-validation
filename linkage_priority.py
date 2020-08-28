import arcpy


class ToolValidator(object):
    """Class for validating a tool's parameter values and controlling
    the behavior of the tool's dialog."""

    def __init__(self):
        """Setup arcpy and the list of tool parameters."""
        self.params = arcpy.GetParameterInfo()

        self.coretbl_param = self.params[11]
        self.expertcoor_param = self.params[14]
        self.core_params = [12, 13, 14]
        self.climrast_param = self.params[15]
        self.modadvance_param = self.params[16]
        self.climate_params = range(17, 28)
        self.expcoorwt_param = self.params[31]
        self.climgradwt_param = self.params[32]

    def initializeParameters(self):
        """Refine the properties of a tool's parameters.
        This method is called when the tool is opened."""

    def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        if self.coretbl_param.value:
            for i in self.core_params:
                self.params[i].enabled = True
        else:
            for i in self.core_params:
                self.params[i].value = None
                self.params[i].enabled = False

        if self.expertcoor_param.value:
            self.expcoorwt_param.enabled = True
        else:
            self.expcoorwt_param.enabled = False

        if self.climrast_param.value:
            self.modadvance_param.enabled = True
            self.climgradwt_param.enabled = True
        else:
            self.modadvance_param.value = False
            self.modadvance_param.enabled = False
            self.climgradwt_param.enabled = False

        if self.modadvance_param.value:
            for i in self.climate_params:
                self.params[i].enabled = True
        else:
            for i in self.climate_params:
                self.params[i].enabled = False
        return

    def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        if self.coretbl_param.value is None:
            for i in self.core_params:
                self.params[i].clearMessage()
        return
