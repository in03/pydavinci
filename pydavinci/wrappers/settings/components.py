# partially generated by datamodel-codegen:
#   filename:  settings.py
#   timestamp: 2022-04-27T02:50:45+00:00

from pathlib import Path
from typing import Any, Optional, Type, Union

from pydantic import BaseModel, DirectoryPath, Field, validator
from pydantic.fields import ModelField
from typing_extensions import Literal

import pydavinci.wrappers.settings.map as map
from pydavinci.wrappers.settings.validator import BaseConfig

StillsNamingPattern = Literal[
    "clipName",
    "versionName",
    "sourceTimecode",
    "timelineTimecode",
    "timelineName",
    "displayLUTName",
    "customLabel",
]

ColorScienceMode = Literal["davinciYRGB", "davinciYRGBColorManagedv2", "acescc", "acescct"]

ImageResizeMode = Literal[
    "smoother",
    "bicubic",
    "bilinear",
    "sharper",
    "box",
    "catrom",
    "cubic",
    "gaussian",
    "lanczos",
    "linear",
    "mitchell",
    "nearestNeighbor",
    "quadratic",
    "sinc",
]

OptimizedCodecs = Literal[
    "rgb",
    "dnxhd_444_12b",
    "dnxhd_hqx_12b",
    "dnxhd_hq",
    "dnxhd_sq",
    "dnxhd_lb",
    "CFHDb64a",
    "CFHDv210",
]


CaptureCodecs = Literal[
    "rgb",
    "dnxhd_720p145",
    "dnxhd_720p220",
    "dnxhd_720p220X",
    "dnxhd_1080i145",
    "dnxhd_1080i220",
    "dnxhd_1080i220X",
    "dnxhd_1080p36",
    "dnxhd_1080p145",
    "dnxhd_1080p220",
    "dnxhd_1080p220X",
    "dnxhd_1080p440X",
    "r210",
    "yuv",
    "v210 ",
]


# fmt: off


class Audio(BaseConfig):
    capture_num_channels: int = Field(alias="audioCaptureNumChannels", ge=2, le=16, multiple_of=2)
    output_has_timecode: bool = Field(alias="audioOutputHasTimecode")
    playout_num_channels: int = Field(alias="audioPlayoutNumChannels", ge=2, le=16, multiple_of=2)
    limit_meter_align_level: int = Field(alias="limitAudioMeterAlignLevel", ge=-30, le=0)
    limit_meter_display_mode: Literal["track_source", "post_fader"] = Field(alias="limitAudioMeterDisplayMode")
    limit_meter_high_level: int = Field(alias="limitAudioMeterHighLevel", ge=-30, le=0)
    limit_meter_lufs: str = Field(alias="limitAudioMeterLUFS")
    limit_meter_loudness_scale: Literal["ebu_18_scale", "ebu_9_scale"] = Field(alias="limitAudioMeterLoudnessScale")
    limit_meter_low_level: int = Field(alias="limitAudioMeterLowLevel", ge=-30, le=0)


    # Putting all of them here also to avoid them going to the top of the list when calling settings.audio
    _selfvalidate: Optional[bool]
    _obj: Optional[Any]




class Color(BaseConfig):
    aces_gamut_compress_type: Optional[Literal["ACES reference gamut compress"]] = Field(alias="colorAcesGamutCompressType")
    aces_idt: str = Field(alias="colorAcesIDT")
    aces_node_lut_processing_space: Literal["acesAp0Linear", "acesccAp1"] = Field(alias="colorAcesNodeLUTProcessingSpace")
    aces_odt: str = Field(alias="colorAcesODT")
    gallery_stills_location: Optional[Union[DirectoryPath, str]] = Field(alias="colorGalleryStillsLocation")
    gallery_stills_naming_custom_pattern: Optional[str] = Field(alias="colorGalleryStillsNamingCustomPattern")
    gallery_stills_naming_enabled: bool = Field(alias="colorGalleryStillsNamingEnabled")
    gallery_stills_naming_pattern: StillsNamingPattern = Field(alias="colorGalleryStillsNamingPattern")
    gallery_stills_naming_with_still_number: Literal["off", "suffix", "prefix"] = Field(alias="colorGalleryStillsNamingWithStillNumber")
    keyframe_dynamics_end_profile: int = Field(alias="colorKeyframeDynamicsEndProfile", ge=0, le=11)
    keyframe_dynamics_start_profile: int = Field(alias="colorKeyframeDynamicsStartProfile", ge=0, le=11)
    color_luminance_mixer_default_zero: bool = Field(alias="colorLuminanceMixerDefaultZero")
    color_science_mode: ColorScienceMode = Field(alias="colorScienceMode")
    color_space_input: str = Field(alias="colorSpaceInput")
    color_space_input_gamma: Optional[str] = Field(alias="colorSpaceInputGamma")
    color_space_output: str = Field(alias="colorSpaceOutput")
    color_space_output_gamma: Optional[str] = Field(alias="colorSpaceOutputGamma")
    color_space_output_gamut_mapping: Optional[str] = Field(alias="colorSpaceOutputGamutMapping")
    color_space_output_gamut_saturation_knee: float = Field(alias="colorSpaceOutputGamutSaturationKnee")
    color_space_output_gamut_saturation_max: str = Field(alias="colorSpaceOutputGamutSaturationMax")
    color_space_output_tone_luminance_max: int = Field(alias="colorSpaceOutputToneLuminanceMax")
    color_space_output_tone_mapping: Optional[str] = Field(alias="colorSpaceOutputToneMapping")
    color_space_timeline: str = Field(alias="colorSpaceTimeline")
    color_space_timeline_gamma: Optional[str] = Field(alias="colorSpaceTimelineGamma")
    use_bgr_pixel_order_for_dpx: bool = Field(alias="colorUseBGRPixelOrderForDPX")
    use_contrast_s_curve: bool = Field(alias="colorUseContrastSCurve")
    use_legacy_log_grades: int = Field(alias="colorUseLegacyLogGrades", ge=1, le=2)
    use_local_versions_as_default: bool = Field(alias="colorUseLocalVersionsAsDefault")
    use_stereo_convergence_for_effects: bool = Field(alias="colorUseStereoConvergenceForEffects")
    version1_name: Optional[str] = Field(alias="colorVersion1Name")
    version2_name: Optional[str] = Field(alias="colorVersion2Name")
    version3_name: Optional[str] = Field(alias="colorVersion3Name")
    version4_name: Optional[str] = Field(alias="colorVersion4Name")
    version5_name: Optional[str] = Field(alias="colorVersion5Name")
    version6_name: Optional[str] = Field(alias="colorVersion6Name")
    version7_name: Optional[str] = Field(alias="colorVersion7Name")
    version8_name: Optional[str] = Field(alias="colorVersion8Name")
    version9_name: Optional[str] = Field(alias="colorVersion9Name")
    version10_name: Optional[str] = Field(alias="colorVersion10Name")
    hdr10_plus_controls_on: bool = Field(alias="hdr10PlusControlsOn")
    hdr_dolby_controls_on: bool = Field(alias="hdrDolbyControlsOn")
    hdr_dolby_master_display: Optional[str] = Field(alias="hdrDolbyMasterDisplay")
    hdr_dolby_version: Literal["4.0", "2.9"] = Field(alias="hdrDolbyVersion")
    hdr_mastering_luminance_max: int = Field(alias="hdrMasteringLuminanceMax", ge=100, le=10000)
    hdr_mastering_on: bool = Field(alias="hdrMasteringOn")
    use_ca_transform: bool = Field(alias="useCATransform")
    use_color_space_aware_grading_tools: bool = Field(alias="useColorSpaceAwareGradingTools")
    use_inverse_drt: bool = Field(alias="useInverseDRT")
    output_drt: Optional[str] = Field(alias="outputDRT")
    output_drt_sat_rolloff_limit: int = Field(alias="outputDRTSatRolloffLimit", ge=500, le=20000)
    output_drt_sat_rolloff_start: int = Field(alias="outputDRTSatRolloffStart", ge=1, le=500)
    rcm_preset_mode: Literal["HDR Rec.2020 Intermediate", "SDR Rec.709", "Custom"] = Field(alias="rcmPresetMode")
    separate_color_space_and_gamma: bool = Field(alias="separateColorSpaceAndGamma")
    input_drt: Optional[Literal["None", "Simple", "Luminance Mapping", "DaVinci", "Saturation Preserving"]] = Field(alias="inputDRT")
    input_drt_sat_rolloff_limit: int = Field(alias="inputDRTSatRolloffLimit", ge=500, le=20000)
    input_drt_sat_rolloff_start: int = Field(alias="inputDRTSatRolloffStart", ge=1, le=500)
    auto_color_manage: bool = Field(alias="isAutoColorManage")
    limit_broadcast_safe_levels: Literal['20_120', '10_110', '0_100'] = Field(alias="limitBroadcastSafeLevels")
    limit_broadcast_safe: bool = Field(alias="limitBroadcastSafeOn")

    _selfvalidate: Optional[bool]
    _obj: Optional[Any]


class Perf(BaseConfig):
    auto_render_cache_after_time: int = Field(alias="perfAutoRenderCacheAfterTime", ge=1, le=30)
    auto_render_cache_composite: bool = Field(alias="perfAutoRenderCacheComposite")
    auto_render_cache_enable: bool = Field(alias="perfAutoRenderCacheEnable")
    auto_render_cache_fu_effect: bool = Field(alias="perfAutoRenderCacheFuEffect")
    auto_render_cache_transition: bool = Field(alias="perfAutoRenderCacheTransition")
    cache_clips_location: Optional[Union[Path, str]] = Field(alias="perfCacheClipsLocation")
    optimised_codec: OptimizedCodecs = Field(alias="perfOptimisedCodec")
    optimised_media_on: bool = Field(alias="perfOptimisedMediaOn")
    optimized_resolution_ratio: Literal["original", "half", "quarter", "one_eighth", "one_sixteenth", "auto"] = Field(alias="perfOptimizedResolutionRatio")
    proxy_media_on: bool = Field(alias="perfProxyMediaOn")
    proxy_resolution_ratio: Literal["original", "half", "quarter"] = Field(alias="perfProxyResolutionRatio")
    render_cache_codec: OptimizedCodecs = Field(alias="perfRenderCacheCodec")
    render_cache_mode: Literal["user", "smart", "none"] = Field(alias="perfRenderCacheMode")

    _selfvalidate: Optional[bool]
    _obj: Optional[Any]

class Deck(BaseConfig):
    add32_pulldown: bool = Field(alias="videoDeckAdd32Pulldown")
    bit_depth: str = Field(alias="videoDeckBitDepth")
    format: str = Field(alias="videoDeckFormat")
    non_auto_edit_frames: bool = Field(alias="videoDeckNonAutoEditFrames")
    output_sync_source: str = Field(alias="videoDeckOutputSyncSource")
    preroll_sec: int = Field(alias="videoDeckPrerollSec", ge=2, le=8)
    sdi_configuration: str = Field(alias="videoDeckSDIConfiguration")
    use444_sdi: bool = Field(alias="videoDeckUse444SDI")
    use_auto_edit: bool = Field(alias="videoDeckUseAudoEdit")
    use_stereo_sdi: bool = Field(alias="videoDeckUseStereoSDI")

    _selfvalidate: Optional[bool]
    _obj: Optional[Any]

class Capture(BaseConfig):
    codec: Optional[CaptureCodecs] = Field(alias="videoCaptureCodec")
    format: Optional[Literal["mov", "dpx"]] = Field(alias="videoCaptureFormat")
    ingest_handles: int = Field(alias="videoCaptureIngestHandles", ge=0, le=9999)
    location: Optional[Union[Path, str]] = Field(alias="videoCaptureLocation")
    mode: Literal["video_only", "video_audio"] = Field(alias="videoCaptureMode")

    _selfvalidate: Optional[bool]
    _obj: Optional[Any]

class Playout(BaseConfig):
    audio_frames_offset: int = Field(alias="videoPlayoutAudioFramesOffset", ge=0, le=99)
    batch_head_duration: int = Field(alias="videoPlayoutBatchHeadDuration", ge=0, le=99)
    batch_tail_duration: int = Field(alias="videoPlayoutBatchTailDuration", ge=0, le=99)
    ltc_frames_offset: int = Field(alias="videoPlayoutLTCFramesOffset", ge=0, le=20)
    mode: Literal["video_only", "audio_only", "video_audio"] = Field(alias="videoPlayoutMode")
    show_ltc: bool = Field(alias="videoPlayoutShowLTC")
    show_source_timecode: bool = Field(alias="videoPlayoutShowSourceTimecode")

    _selfvalidate: Optional[bool]
    _obj: Optional[Any]


class ProjectUniqueSettings(BaseConfig):
    graphics_white_level: int = Field(alias="graphicsWhiteLevel", ge=100, le=4000)
    image_deinterlace_quality: Literal["high", "normal"] = Field(alias="imageDeinterlaceQuality")
    image_enable_field_processing: bool = Field(alias="imageEnableFieldProcessing")
    image_motion_estimation_mode: Literal["enhancedBetter", "enhancedFaster", "standardFaster", "standardBetter"] = Field(alias="imageMotionEstimationMode")
    image_motion_estimation_range: Literal["small", "larger", "medium"] = Field(alias="imageMotionEstimationRange")
    image_resize_mode: ImageResizeMode = Field(alias="imageResizeMode")
    image_resizing_gamma: str = Field(alias="imageResizingGamma")
    image_retime_interpolation: Literal["nearest", "frameBlend", "opticalFlow"] = Field(alias="imageRetimeInterpolation")
    limit_subtitle_cpl: str = Field(alias="limitSubtitleCPL")
    limit_subtitle_caption_duration_sec: int = Field(alias="limitSubtitleCaptionDurationSec", ge=1)
    super_scale_noise_reduction: Literal["Low", "Medium", "High"] = Field(alias="superScaleNoiseReduction")
    super_scale_sharpness: Literal["Low", "Medium", "High"] = Field(alias="superScaleSharpness")
    timeline_frame_rate_mismatch_behavior: Literal["fcp7", "fcpx", "none", "resolve"] = Field(alias="timelineFrameRateMismatchBehavior")
    timeline_input_res_mismatch_custom_preset: Optional[str] = Field(alias="timelineInputResMismatchCustomPreset")
    timeline_input_res_mismatch_use_custom_preset: str = Field(alias="timelineInputResMismatchUseCustomPreset")
    timeline_output_res_mismatch_custom_preset: Optional[str] = Field(alias="timelineOutputResMismatchCustomPreset")
    timeline_output_res_mismatch_use_custom_preset: bool = Field(alias="timelineOutputResMismatchUseCustomPreset")
    timeline_playback_frame_rate: str = Field(alias="timelinePlaybackFrameRate")
    timeline_save_thumbs_in_project: bool = Field(alias="timelineSaveThumbsInProject")
    timeline_working_luminance: int = Field(alias="timelineWorkingLuminance")
    timeline_working_luminance_mode: str = Field(alias="timelineWorkingLuminanceMode")

    _selfvalidate: Optional[bool]
    _obj: Optional[Any]


class TimelineMeta(BaseConfig):


    drop_frame_timecode: bool = Field(alias="timelineDropFrameTimecode")
    frame_rate: float = Field(alias="timelineFrameRate")
    input_res_mismatch_behavior: Literal["centerCrop", "scaleToCrop", "scaleToFit", "stretch"] = Field(alias="timelineInputResMismatchBehavior")
    interlace_processing: bool = Field(alias="timelineInterlaceProcessing")
    output_pixel_aspect_ratio: Literal["square", "cinemascope"] = Field(alias="timelineOutputPixelAspectRatio")
    output_res_match_timeline_res: bool = Field(alias="timelineOutputResMatchTimelineRes")
    output_res_mismatch_behavior: Literal["centerCrop", "scaleToCrop", "scaleToFit", "stretch"] = Field(alias="timelineOutputResMismatchBehavior")
    output_resolution_height: int = Field(alias="timelineOutputResolutionHeight", ge=1)
    output_resolution_width: int = Field(alias="timelineOutputResolutionWidth", ge=1)
    pixel_aspect_ratio: Literal["square", "cinemascope"] = Field(alias="timelinePixelAspectRatio")
    resolution_height: int = Field(alias="timelineResolutionHeight", ge=1)
    resolution_width: int = Field(alias="timelineResolutionWidth", ge=1)

    _selfvalidate: Optional[bool]
    _obj: Optional[Any]

class CommonMonitor(BaseConfig):


    monitor_bit_depth: int = Field(alias="videoMonitorBitDepth")
    monitor_format: str = Field(alias="videoMonitorFormat")
    monitor_matrix_override_for422_sdi: Literal["Rec.2020", "Rec.709", "Rec.601"] = Field(alias="videoMonitorMatrixOverrideFor422SDI")
    monitor_sdi_configuration: Literal["quad_link", "dual_link", "single_link"] = Field(alias="videoMonitorSDIConfiguration")
    monitor_scaling: Literal["bilinear", "basic", "Bilinear", "Basic"] = Field(alias="videoMonitorScaling")  # dirty fix, when setting on timeline it capitalizes first letter, when on project it doesn't... davinci things
    monitor_use444_sdi: bool = Field(alias="videoMonitorUse444SDI")
    monitor_use_hdr_over_hdmi: bool = Field(alias="videoMonitorUseHDROverHDMI")
    monitor_use_level_a: bool = Field(alias="videoMonitorUseLevelA")
    monitor_use_matrix_override_for422_sdi: bool = Field(alias="videoMonitorUseMatrixOverrideFor422SDI")
    monitor_use_stereo_sdi: bool = Field(alias="videoMonitorUseStereoSDI")

    _selfvalidate: Optional[bool]
    _obj: Optional[Any]


class CommonSettings(BaseConfig):

    super_scale: Literal["auto", "no_scaling", "2x", "3x", "4x"] = Field(alias="superScale")
    video_data_levels: Literal["Video", "Full"] = Field(alias="videoDataLevels")
    video_data_levels_retain_subblock_and_super_white_data: bool = Field(alias="videoDataLevelsRetainSubblockAndSuperWhiteData")


    @validator('super_scale')  # type: ignore
    def superscale_validator(cls: Type["BaseModel"], value: Union[int, str], field: 'ModelField') -> Optional[Union[str, int]]:  # type: ignore
        return map.super_scale_transform(value)

class TimelineUniqueSettings(BaseConfig):

    use_custom_settings: bool = Field(alias="useCustomSettings")
