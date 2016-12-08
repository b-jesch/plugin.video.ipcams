import sys
import os
import urllib
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

__addon__ = xbmcaddon.Addon()
__addonID__ = __addon__.getAddonInfo('id')
__path__ = __addon__.getAddonInfo('path')

__LS__ = __addon__.getLocalizedString

'''
def build_url(query):
    return base_url + '?' + urllib.urlencode(query)
'''

def paramsToDict(parameters):

    paramDict = {}
    if parameters:
        paramPairs = parameters.split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

def writeLog(message, level=xbmc.LOGNOTICE):
    xbmc.log('[%s] %s' % (__addonID__, message.encode('utf-8', errors='ignore')), level)

arguments = sys.argv

if len(arguments) > 1:
    if arguments[0][0:6] == 'plugin':
        _addonHandle = int(arguments[1])
        arguments.pop(0)
        arguments[1] = arguments[1][1:]

    params = paramsToDict(arguments[1])
    mode = urllib.unquote_plus(params.get('mode', ''))

if mode is '':
    for i in range(int(__addon__.getSetting('numcams'))):
        icon = xbmc.translatePath(os.path.join( __path__,'resources', 'lib', 'media', 'ipcam_%s.png' % (i + 1)))
        li = xbmcgui.ListItem(__LS__(30011) % (i + 1), iconImage =icon)
        li.setProperty('isPlayable', 'true')
        url = __addon__.getSetting('cam%s' % (i + 1))
        if url != '':
            xbmcplugin.addDirectoryItem(_addonHandle, url, li)

xbmcplugin.endOfDirectory(_addonHandle)