from typing import Any, Dict, List, Optional, Union

class PyRemoteResolve(object):
    def Fusion(self) -> Any: ...
    def GetMediaStorage(self) -> "PyRemoteMediaStorage": ...
    def GetProjectManager(self) -> "PyRemoteProjectManager": ...
    def OpenPage(self, pageName: str) -> bool: ...
    def GetCurrentPage(self) -> str: ...
    def GetProductName(self) -> str: ...
    def GetVersion(self) -> List[Any]: ...
    def GetVersionString(self) -> str: ...
    def LoadLayoutPreset(self, presetName: str) -> bool: ...
    def UpdateLayoutPreset(self, presetName: str) -> bool: ...
    def ExportLayoutPreset(self, presetName: str, presetFilePath: str) -> bool: ...
    def DeleteLayoutPreset(self, presetName: str) -> bool: ...
    def SaveLayoutPreset(self, presetName: str) -> bool: ...
    def ImportLayoutPreset(self, presetFilePath: str, presetName: str) -> bool: ...
    def Quit(self) -> None: ...

class PyRemoteProjectManager(object):
    def CreateProject(self, projectName: str) -> "PyRemoteProject": ...
    def DeleteProject(self, projectName: str) -> bool: ...
    def LoadProject(self, projectName: str) -> "PyRemoteProject": ...
    def GetCurrentProject(self) -> "PyRemoteProject": ...
    def SaveProject(self) -> bool: ...
    def CloseProject(self, project: "PyRemoteProject") -> bool: ...
    def CreateFolder(self, folderName: str) -> bool: ...
    def DeleteFolder(self, folderName: str) -> bool: ...
    def GetProjectListInCurrentFolder(self) -> List[str]: ...
    def GetFolderListInCurrentFolder(self) -> List[str]: ...
    def GotoRootFolder(self) -> bool: ...
    def GotoParentFolder(self) -> bool: ...
    def GetCurrentFolder(self) -> str: ...
    def OpenFolder(self, folderName: str) -> bool: ...
    def ImportProject(self, filePath: str) -> bool: ...
    def ExportProject(self, projectName: str, filePath: str, withStillsAndLUTs: bool) -> bool: ...
    def RestoreProject(self, filePath: str) -> bool: ...
    def GetCurrentDatabase(self) -> Dict[Any, Any]: ...
    def GetDatabaseList(self) -> List[Dict[Any, Any]]: ...
    def SetCurrentDatabase(self, dbInfo: Dict[Any, Any]) -> bool: ...

class PyRemoteProject(object):
    def GetMediaPool(self) -> "PyRemoteMediaPool": ...
    def GetTimelineCount(self) -> int: ...
    def GetTimelineByIndex(self, idx: int) -> "PyRemoteTimeline": ...
    def GetCurrentTimeline(self) -> "PyRemoteTimeline": ...
    def SetCurrentTimeline(self, timeline: "PyRemoteTimeline") -> bool: ...
    def GetGallery(self) -> Optional[Any]: ...
    def GetName(self) -> str: ...
    def SetName(self, projectName: str) -> bool: ...
    def GetPresetList(self) -> List[Any]: ...
    def SetPreset(self, presetName: str) -> bool: ...
    def AddRenderJob(self) -> str: ...
    def DeleteRenderJob(self, jobId: str) -> bool: ...
    def DeleteAllRenderJobs(self) -> bool: ...
    def GetRenderJobList(self) -> List[Any]: ...
    def GetRenderPresetList(self) -> List[Any]: ...
    def StartRendering(
        self, jobids: Optional[List[str]] = ..., isInteractiveMode: bool = ...
    ) -> bool: ...
    def StopRendering(self) -> None: ...
    def IsRenderingInProgress(self) -> bool: ...
    def LoadRenderPreset(self, presetName: str) -> bool: ...
    def SaveAsNewRenderPreset(self, presetName: str) -> bool: ...
    def SetRenderSettings(self, settings: Dict[Any, Any]) -> bool: ...
    def GetRenderJobStatus(self, jobId: str) -> Dict[Any, Any]: ...
    def GetSetting(self, settingName: str) -> Any: ...
    def SetSetting(self, settingName: str, settingValue: Any) -> bool: ...
    def GetRenderFormats(self) -> Dict[Any, Any]: ...
    def GetRenderCodecs(self, renderFormat: str) -> Dict[Any, Any]: ...
    def GetCurrentRenderFormatAndCodec(self) -> Dict[Any, Any]: ...
    def SetCurrentRenderFormatAndCodec(self, format: str, codec: str) -> bool: ...
    def GetCurrentRenderMode(self) -> int: ...
    def SetCurrentRenderMode(self, renderMode: int) -> bool: ...
    def GetRenderResolutions(
        self, format: Optional[str] = ..., codec: Optional[str] = ...
    ) -> List[Dict[Any, Any]]: ...
    def RefreshLUTList(self) -> bool: ...

class PyRemoteMediaStorage(object):
    def GetMountedVolumeList(self) -> List[Any]: ...
    def GetSubFolderList(self, folderPath: str) -> List[Any]: ...
    def GetFileList(self, folderPath: str) -> List[Any]: ...
    def RevealInStorage(self, path: str) -> bool: ...
    def AddItemListToMediaPool(self, items: List[Any]) -> List[Any]: ...
    def AddClipMattesToMediaPool(
        self, MediaPoolItem: "PyRemoteMediaPoolItem", paths: List[Any], stereoEye: str
    ) -> bool: ...
    def AddTimelineMattesToMediaPool(self, paths: List[Any]) -> List[Any]: ...

class PyRemoteMediaPool(object):
    def GetRootFolder(self) -> "PyRemoteFolder": ...
    def AddSubFolder(self, folder: "PyRemoteFolder", name: str) -> "PyRemoteFolder": ...
    def CreateEmptyTimeline(self, name: str) -> "PyRemoteTimeline": ...
    def AppendToTimeline(
        self, clips: List["PyRemoteMediaPoolItem"]
    ) -> List["PyRemoteTimelineItem"]: ...
    def CreateTimelineFromClips(
        self, name: str, clips: List["PyRemoteMediaPoolItem"]
    ) -> "PyRemoteTimeline": ...
    def ImportTimelineFromFile(
        self, filePath: str, options: Optional[Dict[Any, Any]] = ...
    ) -> "PyRemoteTimeline": ...
    def DeleteTimelines(self, timelines: List["PyRemoteTimeline"]) -> bool: ...
    def GetCurrentFolder(self) -> "PyRemoteFolder": ...
    def SetCurrentFolder(self, folder: "PyRemoteFolder") -> bool: ...
    def DeleteClips(self, clips: List["PyRemoteMediaPoolItem"]) -> bool: ...
    def DeleteFolders(self, subfolder: List["PyRemoteFolder"]) -> bool: ...
    def MoveClips(
        self, clips: List["PyRemoteMediaPoolItem"], targetFolder: "PyRemoteFolder"
    ) -> bool: ...
    def MoveFolders(
        self, folder: List["PyRemoteFolder"], targetFolder: "PyRemoteFolder"
    ) -> bool: ...
    def GetClipMatteList(self, MediaPoolItem: "PyRemoteMediaPoolItem") -> List[str]: ...
    def GetTimelineMatteList(self, folder: "PyRemoteFolder") -> List["PyRemoteMediaPoolItem"]: ...
    def DeleteClipMattes(
        self, MediaPoolItem: "PyRemoteMediaPoolItem", paths: List[str]
    ) -> bool: ...
    def RelinkClips(self, clips: List["PyRemoteMediaPoolItem"], folderPath: str) -> bool: ...
    def UnlinkClips(self, clips: List["PyRemoteMediaPoolItem"]) -> bool: ...
    def ImportMedia(self, path: List[str]) -> List["PyRemoteMediaPoolItem"]: ...
    def ExportMetadata(
        self, fileName: str, clips: Optional[List["PyRemoteMediaPoolItem"]] = ...
    ) -> bool: ...

class PyRemoteFolder(object):
    def GetClipList(self) -> List["PyRemoteMediaPoolItem"]: ...
    def GetName(self) -> str: ...
    def GetSubFolderList(self) -> List["PyRemoteFolder"]: ...

class PyRemoteMediaPoolItem(object):
    def GetName(self) -> str: ...
    def GetMetadata(self, metadataType: Optional[Any] = ...) -> Union[Dict[Any, Any], str]: ...
    def SetMetadata(self, metadata: Dict[Any, Any]) -> bool: ...
    def GetMediaId(self) -> str: ...
    def AddMarker(
        self, frameid: int, color: str, name: str, note: str, duration: int, customData: str
    ) -> bool: ...
    def GetMarkers(self) -> Dict[Any, Any]: ...
    def GetMarkerByCustomData(self, customData: str) -> Dict[Any, Any]: ...
    def UpdateMarkerCustomData(self, frameId: int, customData: str) -> bool: ...
    def GetMarkerCustomData(self, frameId: int) -> str: ...
    def DeleteMarkersByColor(self, color: str) -> bool: ...
    def DeleteMarkerAtFrame(self, frameNum: int) -> bool: ...
    def DeleteMarkerByCustomData(self, customData: str) -> bool: ...
    def AddFlag(self, color: str) -> bool: ...
    def GetFlagList(self) -> List[str]: ...
    def ClearFlags(self, color: str) -> bool: ...
    def GetClipColor(self) -> str: ...
    def SetClipColor(self, colorName: str) -> bool: ...
    def ClearClipColor(self) -> bool: ...
    # def GetClipProperty(self, propertyName: Optional[str]) -> Union[str, Dict[Any, Any]]: ...
    def GetClipProperty(self) -> Union[str, Dict[Any, Any]]: ...
    def SetClipProperty(self, propertyName: str, propertyValue: Any) -> bool: ...
    def LinkProxyMedia(self, proxyMediaFilePath: str) -> bool: ...
    def UnlinkProxyMedia(self) -> bool: ...
    def ReplaceClip(self, filePath: str) -> bool: ...

class PyRemoteTimeline(object):
    def GetName(self) -> str: ...
    def SetName(self, timelineName: str) -> bool: ...
    def GetStartFrame(self) -> int: ...
    def GetEndFrame(self) -> int: ...
    def GetTrackCount(self, trackType: str) -> int: ...
    def GetItemListInTrack(self, trackType: str, index: int) -> List["PyRemoteTimelineItem"]: ...
    def AddMarker(
        self, frameid: int, color: str, name: str, note: str, duration: int, customData: str
    ) -> bool: ...
    def GetMarkers(self) -> Dict[Any, Any]: ...
    def GetMarkerByCustomData(self, customData: str) -> Dict[Any, Any]: ...
    def UpdateMarkerCustomData(self, frameId: int, customData: str) -> bool: ...
    def GetMarkerCustomData(self, frameId: int) -> str: ...
    def DeleteMarkersByColor(self, color: str) -> bool: ...
    def DeleteMarkerAtFrame(self, frameNum: int) -> bool: ...
    def DeleteMarkerByCustomData(self, customData: str) -> bool: ...
    def ApplyGradeFromDRX(
        self, path: str, gradeMode: int, items: List["PyRemoteTimelineItem"]
    ) -> bool: ...
    def GetCurrentTimecode(self) -> str: ...
    def SetCurrentTimecode(self, timecode: str) -> bool: ...
    def GetCurrentVideoItem(self) -> "PyRemoteTimelineItem": ...
    def GetCurrentClipThumbnailImage(self) -> Dict[Any, Any]: ...
    def GetTrackName(self, trackType: str, trackIndex: int) -> str: ...
    def SetTrackName(self, trackType: str, trackIndex: int, name: str) -> bool: ...
    def DuplicateTimeline(self, timelineName: Optional[str] = ...) -> "PyRemoteTimeline": ...
    def CreateCompoundClip(
        self, items: List["PyRemoteTimelineItem"], clipinfo: Optional[Dict[Any, Any]] = ...
    ) -> "PyRemoteTimelineItem": ...
    def CreateFusionClip(self, items: List["PyRemoteTimelineItem"]) -> "PyRemoteTimelineItem": ...
    def ImportIntoTimeline(self, filePath: str, importOptions: Dict[Any, Any] = ...) -> bool: ...
    def Export(self, fileName: str, exportType: str, exportSubtype: str) -> bool: ...
    def GetSetting(self, settingName: Optional[Union[str, Dict[Any, Any]]] = ...) -> str: ...
    def SetSetting(
        self, settingName: str, settingValue: Union[str, int, Dict[Any, Any]]
    ) -> bool: ...
    def InsertGeneratorIntoTimeline(self, generatorName: str) -> "PyRemoteTimelineItem": ...
    def InsertFusionGeneratorIntoTimeline(self, generatorName: str) -> "PyRemoteTimelineItem": ...
    def InsertOFXGeneratorIntoTimeline(self, generatorName: str) -> "PyRemoteTimelineItem": ...
    def InsertTitleIntoTimeline(self, titleName: str) -> "PyRemoteTimelineItem": ...
    def InsertFusionTitleIntoTimeline(self, titleName: str) -> "PyRemoteTimelineItem": ...
    def GrabStill(self) -> Any: ...
    def GrabAllStills(self, stillFrameSource: int) -> Any: ...

class PyRemoteTimelineItem(object):
    def GetName(self) -> str: ...
    def GetDuration(self) -> int: ...
    def GetEnd(self) -> int: ...
    def GetFusionCompCount(self) -> int: ...
    def GetFusionCompByIndex(self, compIndex: int) -> Any: ...
    def GetFusionCompNameList(self) -> List[str]: ...
    def GetFusionCompByName(self, compName: str) -> Any: ...
    def GetLeftOffset(self) -> int: ...
    def GetRightOffset(self) -> int: ...
    def GetStart(self) -> int: ...
    def SetProperty(
        self, propertyKey: str, propertyValue: Union[str, int, Dict[Any, Any]]
    ) -> bool: ...
    def GetProperty(self, propertyKey: str) -> Union[str, int, Dict[Any, Any]]: ...
    def AddMarker(
        self, frameid: int, color: str, name: str, note: str, duration: int, customData: str
    ) -> bool: ...
    def GetMarkers(self) -> Dict[Any, Any]: ...
    def GetMarkerByCustomData(self, customData: str) -> Dict[Any, Any]: ...
    def UpdateMarkerCustomData(self, frameId: int, customData: str) -> bool: ...
    def GetMarkerCustomData(self, frameId: int) -> str: ...
    def DeleteMarkersByColor(self, color: str) -> bool: ...
    def DeleteMarkerAtFrame(self, frameNum: int) -> bool: ...
    def DeleteMarkerByCustomData(self, customData: str) -> bool: ...
    def AddFlag(self, color: str) -> bool: ...
    def GetFlagList(self) -> List[str]: ...
    def ClearFlags(self, color: str) -> bool: ...
    def GetClipColor(self) -> str: ...
    def SetClipColor(self, colorName: str) -> bool: ...
    def ClearClipColor(self) -> bool: ...
    def AddFusionComp(self) -> Any: ...
    def ImportFusionComp(self, path: str) -> Any: ...
    def ExportFusionComp(self, path: str, compIndex: int) -> bool: ...
    def DeleteFusionCompByName(self, compName: str) -> bool: ...
    def LoadFusionCompByName(self, compName: str) -> Any: ...
    def RenameFusionCompByName(self, oldName: str, newName: str) -> bool: ...
    def AddVersion(self, versionName: str, versionType: int) -> bool: ...
    def GetCurrentVersion(self) -> Dict[str, int]: ...
    def DeleteVersionByName(self, versionName: str, versionType: int) -> bool: ...
    def LoadVersionByName(self, versionName: str, versionType: int) -> bool: ...
    def RenameVersionByName(self, oldName: str, newName: str, versionType: int) -> bool: ...
    def GetVersionNameList(self, versionType: int) -> List[str]: ...
    def GetMediaPoolItem(self) -> "PyRemoteMediaPoolItem": ...
    def GetStereoConvergenceValues(self) -> Dict[Any, Any]: ...
    def GetStereoLeftFloatingWindowParams(self) -> Dict[Any, Any]: ...
    def GetStereoRightFloatingWindowParams(self) -> Dict[Any, Any]: ...
    def GetNumNodes(self) -> int: ...
    def SetLUT(self, nodeIndex: int, lutPath: str) -> bool: ...
    def GetLUT(self, nodeIndex: int) -> str: ...
    def SetCDL(self, cdl: Dict[str, str]) -> bool: ...
    def AddTake(
        self,
        mediapoolitem: "PyRemoteMediaPoolItem",
        startFrame: Optional[int],
        endFrame: Optional[int],
    ) -> bool: ...
    def GetSelectedTakeIndex(self) -> int: ...
    def GetTakesCount(self) -> int: ...
    def GetTakeByIndex(self, idx: int) -> Dict[Any, Any]: ...
    def DeleteTakeByIndex(self, idx: int) -> bool: ...
    def SelectTakeByIndex(self, idx: int) -> bool: ...
    def FinalizeTake(self) -> bool: ...
    def CopyGrades(self, items: List["PyRemoteTimelineItem"]) -> bool: ...
