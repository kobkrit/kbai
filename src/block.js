Blockly.Blocks['sumorobot_opponent'] = {
    init: function () {
        this.setColour("#0099E6");
        this.appendDummyInput().appendField('opponent');
        this.setOutput(true, 'Boolean');
    }
};
Blockly.Blocks['start_object_detector'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Start object detector");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};